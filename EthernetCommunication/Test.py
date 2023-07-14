import time
import ConfigData

# create a config dta object of ConfigurationData class
confdata = ConfigData.ConfigurationData()


def update_low():
    confdata.update_config("Speed", 45)
    confdata.update_config("Ang", 90)
    confdata.update_config("Type", 'M')
    confdata.update_config("Acc", 5)
    confdata.update_config("Trm", 1)
    confdata.update_config("Pow", 2)
    confdata.update_config("Fal", 0)
    confdata.update_config("Saf", 1)
    time.sleep(2)


def update_high():
    confdata.update_config("Speed", 150)
    confdata.update_config("Ang", 120)
    confdata.update_config("Type", 'S')
    confdata.update_config("Acc", 10)
    confdata.update_config("Trm", 3)
    confdata.update_config("Pow", 2)
    confdata.update_config("Fal", 0)
    confdata.update_config("Saf", 1)
    time.sleep(2)
