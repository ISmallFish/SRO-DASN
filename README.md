# SRO-DASN

---

## RPM Method

The Python implementation of the **RPM (Real Part Maximization)** method proposed in the paper  
*“Online Sampling Rate Offset Estimation via Real Part Maximization”* is available in the `RPM_PythonVer` directory.

We have added inline comments to help align the code with the equations presented in the paper, making it easier to follow and verify.

If you have any questions, feel free to reach out via [gshanzheng@foxmail.com](mailto:gshanzheng@foxmail.com).

---

## Data Generation

### Diffuse Babble Noise

The generation of diffuse babble noise follows the method described in [1].  
The implementation and related source files can be found in the `ANF-Generator-BabbleNoise` directory.

### Data with Sampling Rate Offset (SRO)

We extended the dataset released in [2] to enrich the acoustic scenarios and cover more diverse and realistic conditions.  
This extension is built upon their open-source implementation, which is available at:  
[https://github.com/fgnt/paderwasn/tree/main/paderwasn/databases](https://github.com/fgnt/paderwasn/tree/main/paderwasn/databases)

To support the extended setup, we modified parts of the original data generation pipeline.  
These changes are included in the `SomeMod_DataGen`, specifically in the following files:

- `create_json.py`  
- `write_files.py`  
- `audio_generation.py`

All configuration files — including both initial setup and intermediate outputs — are organized under the directory:  
`SomeMod_DataGen/db_json_sv`

---

## References

[1] E. A. P. Habets, I. Cohen, and S. Gannot, *"Generating nonstationary multisensor signals under a spatial coherence constraint"*,  
**J. Acoust. Soc. Am.**, vol. 124, no. 5, pp. 2911–2917, Nov. 2008.

[2] T. Gburrek, J. Schmalenstroeer, and R. Haeb-Umbach, *"On synchronization of wireless acoustic sensor networks in the presence of time-varying sampling rate offsets and speaker changes"*,  
in **Proc. IEEE Int. Conf. Acoust., Speech, Signal Process. (ICASSP)**, 2022, pp. 916–920.
