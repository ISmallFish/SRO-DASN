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
  We extended the dataset released in [2] to enrich the acoustic scenarios and cover more diverse and realistic conditions.  
  This extension was built upon their open-source implementation, available at:  
  [https://github.com/fgnt/paderwasn/tree/main/paderwasn/databases](https://github.com/fgnt/paderwasn/tree/main/paderwasn/databases)

  To support the extended setup, we made several modifications to the original data generation pipeline.  
  These changes are implemented in the `SomeMod_DataGen` module, specifically in the following files:  
  - `create_json.py`  
  - `write_files.py`  
  - `audio_generation.py`

  In addition, all configuration files related to data generation — including both initial settings and intermediate outputs — are organized under the `SomeMod_DataGen/db_json_sv` directory.

### References

[1] E. A. P. Habets, I. Cohen, and S. Gannot, *"Generating nonstationary multisensor signals under a spatial coherence constraint"*, **J. Acoust. Soc. Am.**, vol. 124, no. 5, pp. 2911–2917, Nov. 2008.

[2] T. Gburrek, J. Schmalenstroeer, and R. Haeb-Umbach, *"On synchronization of wireless acoustic sensor networks in the presence of time-varying sampling rate offsets and speaker changes"*, in *Proc. IEEE Int. Conf. Acoust., Speech, Signal Process. (ICASSP)*, 2022, pp. 916–920.

