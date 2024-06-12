
import pandas as pd
import numpy as np
import csv

sat = pd.read_csv('/Users/manvi/Downloads/merged_sx.csv')
sat['timestamp'] = pd.to_datetime(sat['timestamp'])
sat.set_index('timestamp', inplace=True)
# Define aggregation methods for the specified columns
aggregation_methods = {
    'HTM': 'mean',
    'EXOS_TEMP__Kelvin': 'mean',
    'DRAG_FACTOR__': 'mean',
    'GEOMAG_INDEX__KP__': 'mean',
    #'ECD_LT__hours': 'mean',
    'L-SHELL_VALUE__': 'mean',
    'B-FIELD_MAG.__Gauss': 'mean',
    #'MAG_EQUATOR_LT__hours': 'mean',
    'INVARIANT_LATITUDE__degrees': 'mean',
    'PITCH_ANGLE__degrees': 'mean',
   #'LOSSCONE_100_KM__degrees': 'mean',
   # 'LOSSCONE__<100_KM.__degrees': 'mean',
    'DECLINATION_DEG__degrees': 'mean',
    'DIP_ANGLE__degrees': 'mean',
    'MAG_RAD_DIS_KM__km': 'mean',
    'MAG_INV_LAT.__degrees': 'mean',
    #'CTRL_MODE__': 'mode',
    'COSINE_SUN-B_ANGLE__': 'mean',
    'FLUX:>.6_E-_+_>.8_H+__1/(cm2_s_sr)': 'sum',
    'FLUX:>.6_MEV_E-_&_>.8_MEV_H+__1/(cm2_s_sr)': 'sum',
    'RAD_DIST._(@_Rad_Dist._)_km': 'mean',
    'longitude': 'mean',
    'latitude': 'mean',
    'GEI_X_(@_GEI_X_)_km': 'mean',
    'GEI_Y_(@_GEI_Y_)_km': 'mean',
    'GEI_Z_(@_GEI_Z_)_km': 'mean',
    'VX_GEI_(@_VX_GEI_)_km/s': 'mean',
    'VY_GEI_(@_VY_GEI_)_km/s': 'mean',
    'VZ_GEI_(@_VZ_GEI_)_km/s': 'mean',
#    'DISPACEMENT_(@_Dispacement_)_km': 'mean',
    'BX_GEI_(@_BX_GEI_)_gauss': 'mean',
    'BY_GEI_(@_BY_GEI_)_gauss': 'mean',
    'BZ_GEI_(@_BZ_GEI_)_gauss': 'mean',
    'B_RADIAL_(@_B_radial_)_gauss': 'mean',
    'B_SOUTH_(@_B_South_)_gauss': 'mean',
    'B_EAST_(@_B_East_)_gauss': 'mean',
    'MX_(@_Mx_)_Gauss_RE**3': 'mean',
    'MY_(@_My_)_Gauss_RE**3': 'mean',
    'MZ_(@_Mz_)_Gauss_RE**3': 'mean',
    'DIPOLE_CENTER_X_km': 'mean',
    'DIPOLE_CENTER_Y_km': 'mean',
    'DIPOLE_CENTER_Z_km': 'mean',
    'ME_ALTITUDE_(@_Altitude_)_km': 'mean',
    'ME_LONGITUDE_(@_Longitude_)_deg': 'mean',
    'ME_LATITUDE_(@_Latitude_)_deg': 'mean',
    'ME_B-FIELD_(@_B-Field_)_Gauss': 'mean',
    'S100_ALTITUDE_(@_Altitude_)_km': 'mean',
    'S100_LONGITUDE_(@_Longitude_)_deg': 'mean',
    'S100_LATITUDE_(@_Latitude_)_deg': 'mean',
    'S100_B-FIELD_(@_B-Field_)_Gauss': 'mean',
    'N100_ALTITUDE_(@_Altitude_)_km': 'mean',
    'N100_LONGITUDE_(@_Longitude_)_deg': 'mean',
    'N100_LATITUDE_(@_Latitude_)_deg': 'mean',
    'N100_B-FIELD_(@_B-Field_)_Gauss': 'mean',
    'LICA:0.49-8.3_MEV/N_(@_4.395E+00_MeV/nu)_1/(cm2_sec_sr_MeV/n': 'sum',
    'HILT:8.2-42_MEV/N_(@_2.510E+01_MeV/nu)_1/(cm2_sec_sr_MeV/n': 'sum',
    'MAST:19.3-22.8_MEV/N_(@_2.105E+01_MeV/nu)_1/(cm2_sec_sr_MeV/n': 'sum',
    'MAST:22.8-31.0_MEV/N_(@_2.690E+01_MeV/nu)_1/(cm2_sec_sr_MeV/n': 'sum',
    'MAST:31-51.7_MEV/N_(@_4.135E+01_MeV/nu)_1/(cm2_sec_sr_MeV/n': 'sum',
    'MAST:51.7-76.2_MEV/N_(@_6.395E+01_MeV/nu)_1/(cm2_sec_sr_MeV/n': 'sum',
    'MAST:76.2-113_MEV/N_(@_9.460E+01_MeV/nu)_1/(cm2_sec_sr_MeV/n': 'sum',
    'MAST:113-156_MEV/N_(@_1.345E+02_MeV/nu)_1/(cm2_sec_sr_MeV/n': 'sum',
    'HILT:41-220_MEV/N_(@_1.310E+02_MeV/nu)_1/(cm2_sec_sr_MeV/n': 'sum',
    'LICA:0.5-6.6_MEV/N_(@_3.050E+00_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'HILT:4-9_MEV/N_(@_6.500E+00_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'MAST:8-15_MEV/N_(@_1.150E+01_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'HILT:9-38_MEV/N_(@_2.350E+01_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'MAST:5-12_MEV_(@_8.500E+00_MeV)_1/(cm2_s_sr_MeV/n)': 'sum',
    'PET:19-27_MEV_(@_2.300E+01_MeV)_1/(cm2_s_sr_MeV/n)': 'sum',
    #'PET:1.5-6_MEV_(@_3.750E+00_MeV)_1/(cm2_s_sr_MeV)': 'sum',
    #'PET:2.5-14_MEV_(@_8.250E+00_MeV)_1/(cm2_s_sr_MeV)': 'sum',
    'LICA:0.49-8.3_MEV/N_(@_4.395E+00_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'HILT:8.2-42_MEV/N_(@_2.510E+01_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'MAST:19.3-22.8_MEV/N_(@_2.105E+01_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'MAST:22.8-31.0_MEV/N_(@_2.690E+01_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'MAST:31-51.7_MEV/N_(@_4.135E+01_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'MAST:51.7-76.2_MEV/N_(@_6.395E+01_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'MAST:76.2-113_MEV/N_(@_9.460E+01_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'MAST:113-156_MEV/N_(@_1.345E+02_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'HILT:41-220_MEV/N_(@_1.310E+02_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'LICA:0.5-6.6_MEV/N_(@_3.050E+00_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'HILT:4-9_MEV/N_(@_6.500E+00_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'MAST:8-15_MEV/N_(@_1.150E+01_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'HILT:9-38_MEV/N_(@_2.350E+01_MeV/nu)_1/(cm2_s_sr_MeV/n)': 'sum',
    'MAST:5-12_MEV_(@_8.500E+00_MeV)_1/(cm2_s_sr_MeV/n)': 'sum'

}

# Resample to hourly data using the defined aggregation methods
sat_hourly = sat.resample('H').agg(aggregation_methods)
# Round off values in column 'A' to 2 decimal places
sat_hourly['longitude'] = (sat_hourly['longitude'] / 10).round() * 10
sat_hourly['latitude'] = (sat_hourly['latitude'] / 10).round() * 10
sat_hourly['HTM'] = ((sat_hourly['HTM'] / 25).round() * 25).round(0)