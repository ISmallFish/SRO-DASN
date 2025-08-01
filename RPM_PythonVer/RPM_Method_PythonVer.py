import numpy as np
from scipy.signal.windows import blackman
import matplotlib.pyplot as plt
from tqdm import tqdm
import scipy.io as scio

def func_GenMat_B(L, L_range):

    B_full      = np.tril(np.ones((L, L)))

    row_indices = np.array(L_range) - 1  

    return B_full[row_indices, :]

# ========================================================================= #
#         Configuration of the Hyperparameters of RPM Method.               #
# ========================================================================= #

K          = 4096            
Kh         = 2048    
epsilon    = 1.0e-12     
lamda_1    = 0.80  
lamda_2    = 0.20
gamma      = 0.975
Ls         = 12
Lh         = 2

# ------------------------------------------------------------------------- #

L          = Ls*Lh
window     = blackman(K, sym = False) 


idx_left   = np.arange(L-2,-1,-Lh)
idx_right  = L*np.ones_like(idx_left)

fs         = 16000           
dtype      = np.complex128

f          = (2 * np.pi * np.arange(0, K//2 + 1) / K * Kh / fs)[:, np.newaxis] 
vec_ell    = np.arange(Lh,L+1,Lh)[:, np.newaxis] # \boldsymbol{\ell}

# $\mathbf{C} = \frac{2 \pi }{K} \boldsymbol{\ell} \mathbf{k}^{T} K_{\rm h}$ in eq.(40)
C          = vec_ell @ f.T

w          = Lh / vec_ell # \tilde{\boldsymbol{\ell}} see eq.(41)

# ========================================================================= #
#                                  Data Load                                #
# ========================================================================= #

data_mat   = scio.loadmat('demo_src_file.mat')
x          = data_mat['x']
x1         = x[:, 0]
x2         = x[:, 1]
sro_MtLb   = data_mat['sro_Arr']

nfrm       = (len(x) - K) // Kh + 1

# ========================================================================= #

X1          = np.zeros((K//2+1,  nfrm), dtype = dtype)
X2          = np.zeros((K//2+1,  nfrm), dtype = dtype)
buff_NCS    = np.zeros((K//2+1,   L+1), dtype = dtype)


sro_Arr     = np.zeros((nfrm,1))

for cal_RTF in tqdm(range(100)): # for cal RTF

    for ell in range(nfrm):

        # ell is corresponding to $\ell$ 
        nf             = ell - L + 1 # L = L_s * L_h
        
        start          = ell * Kh
        end            = start + K
        frame1         = x1[start:end] * window
        frame2         = x2[start:end] * window
        
        X1[:, ell]       = np.fft.rfft(frame1, n = K)
        X2[:, ell]       = np.fft.rfft(frame2, n = K)

        # eq.(7)
        CS             = X1[:, ell]*np.conj(X2[:, ell])
        NCS            = CS/(np.abs(CS) + epsilon)

        buff_NCS       = np.hstack([buff_NCS[:, 1:], NCS[:, np.newaxis]])

        if nf >= 1: # i.e., ell >= L_s * L_h
            
            # time-varying forgetting factor
            # $ \gamma(l) = 1 - \frac{1 - \gamma}{1 - \gamma^{l - L_{\rm s} L_{\rm h}}}$ in eq.(43)
            gamma_tv       = 1 - (1 - gamma)/(1 - gamma**nf)

            # SNCS
            # Get $\mathbf{\Gamma}(l)$ in eq.(43)
            Phi_Left       = buff_NCS[:,  idx_left]
            Phi_Right      = buff_NCS[:, idx_right]
            Gamma          = (Phi_Left*np.conj(Phi_Right)).T # reshape -> $L_{\rm s} \times {\left(\frac{K}{2} + 1 \right)}$
            
            if nf == 1:
                
                tilde_Gamma = Gamma # initialization

                X_past      = 0.00  # \hat{\varepsilon}(l - 1) see eq.(48)

                X_past_past = 0.00  # \hat{\varepsilon}(l)     see eq.(48)


            # eq.(43) get smoothed SNCS
            tilde_Gamma     = gamma_tv*tilde_Gamma  + (1 - gamma_tv)*Gamma

            # eq.(48)
            X_lookahead     = X_past + lamda_1 * (X_past - X_past_past) 
            

            # eq.(47)
            Re_tilde_Gamma  = np.real(tilde_Gamma)
            Im_tilde_Gamma  = np.imag(tilde_Gamma)
            SinX            = np.sin(C * X_lookahead)
            CosX            = np.cos(C * X_lookahead)
            scale           = w.T @ np.sum(np.abs(tilde_Gamma), axis = 1, keepdims=True)
            grad            = w.T @ np.sum((-Re_tilde_Gamma * SinX + Im_tilde_Gamma * CosX) * C, axis = 1, keepdims=True) / scale

            # eq.(49)
            X_curr          = X_lookahead + lamda_2 * grad
            # ------------------------------------------------- #
            sro_Arr[ell]      = X_curr
            X_past_past     = X_past
            X_past          = X_curr
            

sro_MtLb = np.vstack((np.zeros((L,1)), sro_MtLb))

sro_Arr  = 1e6*sro_Arr/16e3
sro_MtLb = 1e6*sro_MtLb/16e3

plt.plot(sro_Arr,  label='Python - Res')
plt.plot(sro_MtLb, label='MatLab - Res')
plt.legend()
plt.show()

