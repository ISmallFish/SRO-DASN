# SRO-DASN

## RPM Method

The Python implementation of the **RPM (real part maximization)** method proposed in the paper *"Online Sampling Rate Offset Estimation via Real Part Maximization"* can be found in the file `RPM_PythonVer`. 

Some comments have been added to help align the code with the corresponding equations in the paper.

If you have any questions, feel free to contact me at 📧 [gshanzheng@foxmail.com](mailto:gshanzheng@foxmail.com).

You're also welcome to explore, use, or improve the code as part of this open-source project!

## Data Generation

- **Diffuse Babble Noise Generation**  
  The generation of diffuse babble noise follows the method described in [1].  
  The corresponding implementation and source files can be found in the `ANF-Generator-BabbleNoise` directory.

- **Data with Sampling Rate Offset (SRO)**  
  This is based on the method described in [2], and we have extended the original dataset accordingly.  
  Since the extended dataset is developed based on [2], we made some adjustments to the original data generation code.  
  The specific modifications can be found in `SomeMod_DataGen' named:  
  - `create_json.py`  
  - `write_files.py`  
  - `audio_generation.py`

- **Configuration Files**  
  All configuration files related to data generation (including initial and intermediate files) are located in the `SomeMod_DataGen\db_json_sv` folder.
### References

[1] E. A. P. Habets, I. Cohen, and S. Gannot, *"Generating nonstationary multisensor signals under a spatial coherence constraint"*, **J. Acoust. Soc. Am.**, vol. 124, no. 5, pp. 2911–2917, Nov. 2008.

[2] T. Gburrek, J. Schmalenstroeer, and R. Haeb-Umbach, *"On synchronization of wireless acoustic sensor networks in the presence of time-varying sampling rate offsets and speaker changes"*, in *Proc. IEEE Int. Conf. Acoust., Speech, Signal Process. (ICASSP)*, 2022, pp. 916–920.

