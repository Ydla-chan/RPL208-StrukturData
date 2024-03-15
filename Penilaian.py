from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

edge_driver_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
dataList = [
    {"nim": "4342301021", "name": "Absar Rakha Zafran"},
    {"nim": "4342301009", "name": "Aldo Rizki Mukhtar"},
    {"nim": "4342301024", "name": "Bowen Riandu Siahaan"},
    {"nim": "4342301001", "name": "Rahel Simanjuntak"},
    {"nim": "4342301019", "name": "Ririn Fitri Wulandari"},
    {"nim": "4342301030", "name": "Yocelyn Theona Setiawan"},
    {"nim": "4342301026", "name": "Ahmad Ghulam Zaki"},
    {"nim": "4342301006", "name": "Juwita Cahaya Safira"},
    {"nim": "4342301018", "name": "Miftahul Fazra"},
    {"nim": "4342301002", "name": "Mira Handayani"},
    {"nim": "4342301029", "name": "Mufasirina Haqulianti"},
    {"nim": "4342301015", "name": "Muhammad Afif Al Fawwaz"},
    {"nim": "4342301023", "name": "Tabina Rahmah Az Zahrawani"},
    {"nim": "4342301007", "name": "Amelia Hanif"},
    {"nim": "4342301014", "name": "Fitri Reza"},
    {"nim": "4342301027", "name": "Nurul Aini"},
    {"nim": "4342301017", "name": "Dwi Nurul Azizah"},
    {"nim": "4342301007", "name": "Nofri Fahsyuliardi"},
    {"nim": "4342301025", "name": "Jonathan Christian Nainggolan"},
]


def isiNilai(namaKamu, nimKamu, temanKamu, nimTeman):
    nama = driver.find_element(
        by="xpath",
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    nama.send_keys(namaKamu)
    time.sleep(0.1)

    nim = driver.find_element(
        by="xpath",
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    nim.send_keys(nimKamu)
    time.sleep(0.1)

    tim = driver.find_element(
        by="xpath",
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]",
    )
    tim.click()
    time.sleep(0.3)

    timChildren = driver.find_element(
        by="xpath",
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]",
    )
    timChildren.click()
    time.sleep(0.1)

    namaTeman = driver.find_element(
        by="xpath",
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    namaTeman.send_keys(temanKamu)
    time.sleep(0.1)

    namaTeman = driver.find_element(
        by="xpath",
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    namaTeman.send_keys(nimTeman)
    time.sleep(0.1)

    nilaiTeman = driver.find_element(
        by="xpath",
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[1]",
    )
    nilaiTeman.click()
    time.sleep(0.3)

    nilaiChildren = driver.find_element(
        by="xpath",
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div[6]",
    )
    nilaiChildren.click()
    time.sleep(0.1)

    sabmit = driver.find_element(
        by="xpath",
        value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div",
    )
    sabmit.click()
    time.sleep(0.5)


for data in dataList:
    driver = webdriver.Edge()
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSdT1E8mHbq3rN2sSb12Q-C7c321Q2Jf7NEweVti10ufugxdYw/viewform"
    )
    time.sleep(3)
    isiNilai("Aldy Jhonatan Hutasoit", "4342301003", data["name"], data["nim"])
    time.sleep(3)
    driver.quit()

print("PROGRAM SELESAI ^_^")