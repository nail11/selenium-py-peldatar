def find_element(site, id):
    # site = input('Mi a keresett azonosító? ', site)
    # id = input('Mi a keresett azonosító? ', id)

    from selenium import webdriver

    driver = webdriver.Chrome()

    driver.get(site)

    try:
        driver.find_element_by_id(str(id))

    except:
        print("A" + "'" + id + "'" + "azonosítójú elem nem létezik")

    finally:
        driver.close()


site = input('Mi az url? ')
id = input('Mi a keresett azonosító? ')

find_element(site, id)
