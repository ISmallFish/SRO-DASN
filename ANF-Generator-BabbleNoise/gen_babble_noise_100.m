clc;
clear all;
close all;

addpath('./functions');

% tgt dir
target_dir = '.\babble_noise_100_SV';

load node_positions.mat;

%% Initialization

Fs = 16000;                     % Sample frequency (Hz)
params.Fs = Fs;
K = 4096;                       % FFT length
params.K = K;
sc_type = 'spherical';          % Noise-field coherence model: 'corcos', 'spherical', 'cylindrical'
decomposition = 'EVD';          % Type of decomposition: 'EVD' or 'CHD'
processing = 'balanced+smooth'; % Processing method: 'standard', 'smooth', 'balanced', 'balanced+smooth'
dur = 320;                      % Input duration in seconds
L   = dur*Fs;                   % Data length

% Additional parameter for the Corcos model
params.speed     = 20;          % km/h
params.direction = 60;          % Degree w.r.t. "North" (y-axis) [anti-clockwise]

for i = 0:99

    folder_name = sprintf('example_%d', i);

    mm          = squeeze(positions(i+1, :, :));

    M = length(mm(:,1));            % Number of channels
    params.mm = mm;

    % Summary of parameters
    fprintf('Number of channels: %d\n',M)
    fprintf('Spatial coherence: %s\n',sc_type)
    fprintf('Decomposition: %s\n',decomposition)
    fprintf('Processing: %s\n\n',processing)

    %% Generate target spatial coherence

    % Generate target spatial coherence
    DC = generate_target_coherence(sc_type,params);

    %% Generate and evaluate mixing matrix

    % Generate mixing matrix with target spatial coherence (optional balanced/smooth)
    [C, C_none] = mixing_matrix(DC,decomposition,processing);

    % Evaluate balance and smoothness before and after applying the chosen processing method
    % evaluate_mixing_matrix(C_none,C,decomposition,processing,params,sc_type);

    %% Generate signsls with desired spatial coherence

    % Generate M mutually 'independent' babble speech input signals
    [data,Fs_data] = audioread('babble_16kHz.wav');
    data           = kron(data, ones(10, 1));
    if Fs ~= Fs_data
        error('Sample frequency of input file is incorrect.');
    end
    data = data - mean(data);
    babble = zeros(L,M);
    for m=1:M
        babble(:,m) = data((m-1)*L+1:m*L);
    end

    % Generate sensor signals with target spatial coherence
    x = mix_signals(babble,C);

    % Save babble speech
    if ~exist(target_dir, 'dir')
        mkdir(target_dir);
    end

    audiowrite(fullfile(target_dir, [folder_name, '.wav']), x, Fs);

    close all;
    clc;

    disp('==============================');
    disp(folder_name);
    disp('==============================');

end
