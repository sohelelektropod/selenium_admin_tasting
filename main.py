import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AdminPanel:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://devadmin.elektropod.com/admin/')
        self.driver.find_element(By.ID, 'id_username').send_keys("sohel.mulla@elektropod.com")
        self.driver.find_element(By.ID, 'id_password').send_keys("admin")
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'input[value="Log in"]')
        login_button.click()

    def logout(self):
        logout_button = self.driver.find_element(By.XPATH, "//a[normalize-space()='Log out']")
        logout_button.click()

    def click_element(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)

    def groups_XPATH(self):
        self.login()

        # Navigate to Add group page
        self.click_element("//a[normalize-space()='Groups']")
        self.click_element("//a[normalize-space()='Add group']")

        # Fill group name
        self.driver.find_element(By.XPATH, "//input[@id='id_name']").send_keys("testing service_2")

        # Add permissions
        permissions = ["admin | log entry | Can view log entry", "auth | group | Can view group"]
        for permission in permissions:
            self.click_element(f"//option[@title='{permission}']")
            self.click_element("//a[@id='id_permissions_add_link']")

        self.click_element("//input[@name='_save']")
        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("testing")
        self.click_element("//input[@value='Search']")

        # View group details
        self.click_element("//a[normalize-space()='testing service']")
        self.click_element("//a[@class='historylink']")

        # Navigate back to Groups
        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='Groups']")
        self.logout()

    def cs_model_XPATH(self):
        self.login()

        # Navigate to CS Models
        self.click_element("//a[normalize-space()='CS Models']")
        self.click_element("//a[normalize-space()='30KW CCS2']")

        # View history and navigate back to CS Models
        self.click_element("//a[@class='historylink']")
        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='CS Models']")

        # Add CS Model
        self.click_element("//a[normalize-space()='Add CS Model']")
        self.click_element("//a[@href='/admin/csms/csmodel/add/']")

        # Add CS Model form test
        self.driver.find_element(By.XPATH, "//input[@id='id_name']").send_keys("2W-3")
        self.driver.find_element(By.XPATH, "//input[@id='id_evse_count']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='id_evse_count']").send_keys("2")

        connector_type = Select(self.driver.find_element(By.XPATH, "//select[@id='id_connector_type']"))
        connector_type.select_by_visible_text("3-pin Plug")

        self.driver.find_element(By.XPATH, "//input[@id='id_max_output']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='id_max_output']").send_keys("4")
        self.driver.find_element(By.XPATH, "//input[@name='_save']").click()
        self.logout()

    def csms_XPATH(self):

        self.login()

        # Click on 'Charging Stations' link in the sidebar
        self.click_element("a[href='/admin/csms/chargingstation/']")

        # Iterate through site names and select them in the filter
        site_names = ['All', 'Eastwood Layout', 'Surat-Amroli', 'Surat-Nitech',
                      'BHive-HSR Layout', 'Vega City-BLR', 'Padmavati Foundry',
                      'MANGALAM INTERMEDIATES UNIT 2', 'Eastwood_2CDemo', 'Shraddha Motors -TATA Motors']

        for site_name in site_names:
            select_element = Select(self.driver.find_element(By.XPATH, "//select[@class='form-control']"))
            select_element.select_by_visible_text(site_name)

        self.click_element("//a[contains(text(),'✖ Clear all filters')]")

        # Iterate through pagination links
        for page_number in range(1, 3):
            self.click_element(f"//p[1]//a[{page_number}]")

        # Search for 'Sahil' and click on the user link
        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("Sahil")
        self.click_element("//input[@value='Search']")
        self.click_element("//a[normalize-space()='Sahil']")
        self.click_element("//a[@class='historylink']")

        # Click on the 'Sahil' link again and navigate to the 'Charging Stations' section
        self.click_element("//a[normalize-space()='Sahil']")
        self.click_element("//a[@class='configlink']")
        self.driver.find_element(By.XPATH, "//input[@id='id_PlatformCtrlr: Name']").send_keys("TestCharger2")
        self.click_element("//input[@value='Submit']")
        self.click_element("//a[normalize-space()='Charging Stations']")

        # Navigate to 'Add Charging Station' and fill in the details
        self.click_element("//a[@href='/admin/csms/chargingstation/add/']")
        self.click_element("//a[normalize-space()='Charging Stations']")
        self.click_element("//a[normalize-space()='Add Charging Station']")
        self.driver.find_element(By.XPATH, "//input[@id='id_device_id']").send_keys("12345676")
        self.driver.find_element(By.XPATH, "//input[@id='id_product_id']").send_keys("test_selenium_6")
        self.driver.find_element(By.XPATH, "//input[@id='id_name']").send_keys("test_selenium_cs_6")

        # Select values from dropdowns
        select_element = Select(self.driver.find_element(By.XPATH, "//select[@id='id_cs_model']"))
        select_element.select_by_visible_text("2ww")
        time.sleep(2)

        select_element = Select(self.driver.find_element(By.XPATH, "//select[@id='id_firmware_version']"))
        select_element.select_by_visible_text("2.0.32")

        select_element = Select(self.driver.find_element(By.XPATH, "//select[@id='id_cs_site']"))
        select_element.select_by_visible_text("testing_site_selenium")

        # Enter coordinates and save
        self.driver.find_element(By.XPATH, "//textarea[@id='id_location']").send_keys(
            '{"type":"Point","coordinates":[76.924982,18.051173]}')
        self.click_element("//input[@name='_save']")

        # Navigate to 'Config' and force update site
        self.click_element("//a[@class='configlink']")
        select_element = Select(self.driver.find_element(By.XPATH, "//select[@id='id_site']"))
        select_element.select_by_visible_text("testing_site_selenium")
        self.driver.find_element(By.XPATH, "//option[normalize-space()='testing_selenium_cs']").click()
        self.click_element("//input[@value='Submit']")

        # Navigate to 'Home' and then to 'Charging Stations'
        self.click_element("//a[normalize-space()='Home']")
        self.click_element("//a[normalize-space()='Charging Stations']")

        self.logout()

    def firmware_version_XPATH(self):
        self.login()

        # Add Firmware Version
        self.click_element("//a[normalize-space()='Firmware Versions']")  # Firmware version link
        self.click_element("//a[normalize-space()='Add Firmware Version']")

        # Fill details
        self.driver.find_element(By.XPATH, "//input[@id='id_version_name']").send_keys("selenium_test_3.0")
        fv_add_cs_model_select = Select(self.driver.find_element(By.XPATH, "//select[@id='id_cs_model']"))
        fv_add_cs_model_select.select_by_visible_text("2ww")
        self.driver.find_element(By.XPATH, "//textarea[@id='id_config']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='id_config']").send_keys('[{"variable": {"name": "ModelNumber"}, "component": {"name": "PlatformCtrlr"}, "attributeValue": "60KW CCS2", "attributeVarType": "CONFIG_RO", "attributeValueType": "stringType", "attributeFactoryDefValue": "60KW CCS2"}, {"variable": {"name": "FirmwareVersion"}, "component": {"name": "PlatformCtrlr"}, "attributeValue": "3.2.19-2.1.6", "attributeVarType": "CONFIG_RO", "attributeValueType": "stringType", "attributeFactoryDefValue": "3.2.19-2.1.6"}, {"variable": {"name": "Name"}, "component": {"name": "PlatformCtrlr"}, "attributeValue": "TestCharger3", "attributeVarType": "CONFIG_RW", "attributeValueType": "stringType", "attributeFactoryDefValue": "Undefined"}, {"variable": {"name": "Available"}, "component": {"evse": {"id": "1"}, "name": "ChargingStation"}, "attributeValue": "1", "attributeVarType": "CONFIG_RO", "attributeValueType": "boolType", "attributeFactoryDefValue": "1"}, {"variable": {"name": "Available"}, "component": {"evse": {"id": "2"}, "name": "ChargingStation"}, "attributeValue": "1", "attributeVarType": "CONFIG_RO", "attributeValueType": "boolType", "attributeFactoryDefValue": "1"}, {"variable": {"name": "Available"}, "component": {"evse": {"id": "0"}, "name": "ChargingStation"}, "attributeValue": "1", "attributeVarType": "CONFIG_RO", "attributeValueType": "boolType", "attributeFactoryDefValue": "1"}, {"variable": {"name": "AvailabilityState"}, "component": {"name": "ChargingStation"}, "attributeValue": "", "attributeVarType": "STATE_V", "attributeValueType": "stringType", "attributeFactoryDefValue": "Undefined"}, {"variable": {"name": "AvailabilityState"}, "component": {"evse": {"id": "1"}, "name": "ChargingStation"}, "attributeValue": "", "attributeVarType": "STATE_V", "attributeValueType": "stringType", "attributeFactoryDefValue": "Undefined"}, {"variable": {"name": "AvailabilityState"}, "component": {"evse": {"id": "2"}, "name": "ChargingStation"}, "attributeValue": "", "attributeVarType": "STATE_V", "attributeValueType": "stringType", "attributeFactoryDefValue": "Undefined"}, {"variable": {"name": "AvailabilityState"}, "component": {"evse": {"id": "0"}, "name": "ChargingStation"}, "attributeValue": "1", "attributeVarType": "STATE_V", "attributeValueType": "stringType", "attributeFactoryDefValue": "Undefined"}]')

        # Save and view details
        self.click_element("//input[@name='_save']")
        self.click_element("//a[normalize-space()='selenium_test_2.0']")
        self.click_element("//a[@class='historylink']")

        # Navigate back to Firmware Versions
        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='Firmware Versions']")
        self.logout()

    def sites_XPATH(self):
        self.login()

        # Navigate to Sites
        self.click_element("//a[normalize-space()='Sites']")
        self.click_element("//a[normalize-space()='Shraddha Motors -TATA Motors']")

        # View history and navigate back to Sites
        self.click_element("//a[@class='historylink']")
        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='Sites']")

        # Add site
        self.click_element("//a[normalize-space()='Add site']")
        self.click_element("//a[@href='/admin/csms/site/add/'][normalize-space()='Add']")

        # Add site form test
        self.driver.find_element(By.XPATH, "//input[@id='id_name']").send_keys("testing_site_selenium_2")

        site_status_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@id='id_site_status']"))
        site_status_dropdown.select_by_visible_text("Upcoming")

        self.driver.find_element(By.XPATH, "//input[@id='id_site_contact']").send_keys("9420053194")
        self.driver.find_element(By.XPATH, "//input[@id='id_site_address']").send_keys("Bengaluru")

        state_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@id='id_site_state']"))
        state_dropdown.select_by_visible_text("Karnataka")

        self.driver.find_element(By.XPATH, "//input[@id='id_is_owner']").click()

        self.driver.find_element(By.XPATH, "//input[@id='id_invoice_name']").send_keys("sohel mulla one")
        self.driver.find_element(By.XPATH, "//input[@id='id_account_name']").send_keys("sohel mulla one")
        self.driver.find_element(By.XPATH, "//input[@id='id_account_number']").send_keys("1234567891")
        self.driver.find_element(By.XPATH, "//input[@id='id_bank_ifsc']").send_keys("ICICI0000594")

        self.click_element("//input[@name='_save']")
        self.logout()

    def ticket_XPATH(self):
        self.login()

        for title in ['Charging Pod or a socket/gun related issue', 'RFID Card related issue',
                      'Billing or payment related issue', 'Mobile App related issue', 'Other issues']:
            self.click_element(f"//a[@title='{title}']")  # Click on the specific ticket category

        self.click_element("//a[contains(text(),'✖ Clear all filters')]")  # Clear all filters

        for page_number in range(1, 8):
            self.click_element(f'//p[1]//a[{page_number}]')  # Click on pagination link

        self.click_element("//p[1]//a[9]")  # Click on a specific page link
        self.click_element("//a[normalize-space()='hjghjghj']")  # Click on a specific ticket
        self.click_element("//a[@class='historylink']")  # Click on the 'History' link

        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='Tickets']")  # Navigate back to 'Tickets'
        self.click_element("//a[normalize-space()='Add ticket']")  # Click on 'Add ticket' link
        self.click_element("//a[@href='/admin/custms/ticket/add/']")  # Click on 'Add' link to add a new ticket
        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='Tickets']")  # Navigate back to 'Tickets'
        self.logout()

    def users_XPATH(self):

        self.login()  # Login to the system

        self.click_element("//a[normalize-space()='Users']")  # Click on 'User'

        changelist_element = self.driver.find_element(By.ID, 'changelist')

        relative_xpath = ".//ul[1]//li[1]//a[1]"
        changelist_element.find_element(By.XPATH, relative_xpath).click()

        self.click_element("//ul[1]//li[2]//a[1]")
        self.click_element("//ul[1]//li[3]//a[1]")
        self.click_element("//ul[2]//li[1]//a[1]")
        self.click_element("//ul[2]//li[2]//a[1]")
        self.click_element("//ul[2]//li[3]//a[1]")
        self.click_element("//ul[3]//li[1]//a[1]")
        self.click_element("//ul[3]//li[2]//a[1]")
        self.click_element("//ul[3]//li[3]//a[1]")
        self.click_element("//ul[4]//li[1]//a[1]")
        self.click_element("//ul[4]//li[2]//a[1]")
        self.click_element("//ul[5]//li[1]//a[1]")

        self.click_element("//a[@title='customer service']")  # Click on 'customer service' link
        self.click_element("//a[contains(text(),'✖ Clear all filters')]")  # Clear all filters

        for page_number in range(1, 5):
            self.click_element(f'//p[1]//a[{page_number}]')  # pagination links

        self.click_element("//p[1]//a[5]")  # Click on a specific page link
        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("sohel")  # Enter search keyword
        self.click_element("//input[@value='Search']")  # Click on the 'Search' button

        self.click_element(
            "//a[normalize-space()='mullasohelvajir@gmail.com']")  # Click on a specific user's email link
        self.click_element("//a[@class='historylink']")  # Click on the 'History' link

        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='Users']")  # Navigate back to 'Users'
        self.click_element("//a[normalize-space()='Add user']")  # Click on 'Add user' link
        self.click_element("//a[@href='/admin/custms/user/add/']")  # Click on 'Add' link to add a new user
        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='Users']")  # Navigate back to 'Users'

        self.logout()  # Logout from the system

    def txnms_XPATH(self):
        self.login()

        self.click_element("//a[normalize-space()='Transactions']")

        for title in ['All', 'Yes', 'No']:
            self.click_element(f"//a[@title='{title}']")  # filters

        site_names = [
            'All', 'Eastwood Layout', 'Surat-Amroli', 'Surat-Nitech',
            'BHive-HSR Layout', 'Vega City-BLR', 'Padmavati Foundry',
            'MANGALAM INTERMEDIATES UNIT 2', 'Eastwood_2CDemo', 'Shraddha Motors -TATA Motors'
        ]

        for site_name in site_names:
            dropdown = Select(self.driver.find_element(By.XPATH,
                                                       "//ul[@class='admin-filter-CSSite']//select[@class='form-control']"))
            dropdown.select_by_visible_text(site_name)

        charger_names = [
            "TestCharger1", "TestCharger2", "TestCharger3",
            "C1_ABCDE_Sahil", "C1_ABCDE_Mahesh", "C1_ABCDE_Jaydip",
            "VivekTest1", "Sample2", "NodeMCU2", "Jaydip_1C",
            "EP1C1513K22", "Eastwood-1", "Eastwood-2", "EP2C1512K22",
            "4W_2C_Delivery", "1C_Delivery", "4W_2C_Delivery_Extra",
            "NODE_MCU_JD", "Jaydip_Test_Setup", "ChinaTest", "EP2Cfake_delete",
            "EP2C1507K22", "EP2C1508K22", "EP1C1501K22", "EP1C1502K22",
            "EP2C1509K22", "EP2C1510K22", "EP1C1503K22", "EP1C1504K22",
            "EP1C1505K22", "EP1C1506K22", "EP1C1519K22 (Sahil Test)",
            "EP2C1511K22", "EP1C1514K22", "EP1C1516K22", "EP1C1517K22",
            "EP1C1518K22", "EP2C1524D23", "EP1C1521K22 (4Wx1)", "EP1C1522K22",
            "EP1C1523K22 (4Wx1) JaydipTest", "EP1C1530D23 (4Wx1)", "TEST_6_ 4Wx1", "EP1C1534D23",
            "TEST_8_ 4Wx2", "EP1C1532D23",
            "EP1C1545J23", "Jaydip_Office", "Sahil", "ST2C1517K22", "ST2C1518K22"
        ]

        for charger_name in charger_names:
            dropdown = Select(self.driver.find_element(By.XPATH,
                                                       "//ul[@class='admin-filter-chargingstation']//select[@class='form-control']"))
            dropdown.select_by_visible_text(charger_name)

        for title in ['Any date', 'Today', 'Past 7 days', 'This month', 'This year', 'No date', 'Has date']:
            self.click_element(f"//a[@title='{title}']")

        self.click_element("//a[contains(text(),'✖ Clear all filters')]")

        for page_number in range(1, 9):
            self.click_element(f'//p[1]//a[{page_number}]') # pagination

        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("sohel") # Searching for 'sohel'
        self.click_element("//input[@value='Search']")

        self.click_element("//a[normalize-space()='e6fe656d-8905-2bd6-62be-4dc1af359394']")  # view txn
        self.click_element("//a[@class='historylink']")  # 'History'
        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='Transactions']")  # Navigating to'txn'

        self.click_element("//a[@class='reportlink']")  # 'Report'
        self.driver.find_element(By.XPATH, "//input[@id='id_start_date']").send_keys("01/12/2022")
        self.driver.find_element(By.XPATH, "//input[@id='id_end_date']").send_keys("01/12/2023")

        site_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@id='id_site']"))   # Selecting
        site_dropdown.select_by_visible_text("Eastwood Layout")

        self.driver.find_element(By.XPATH, "//input[@value='Submit']").click()

        self.click_element("//a[normalize-space()='Home']")
        self.click_element("//a[normalize-space()='Transactions']")  # Navigating back

        self.logout()

    def wallet_history_XPATH(self):

        self.login()
        self.click_element("//a[normalize-space()='Wallet Historys']")

        # Perform various actions on wallet history records
        for title in ['Yes', 'No', 'Credit', 'Debit']:
            self.click_element(f"//a[@title='{title}']")

        # Clear filters and navigate through pagination
        self.click_element("//a[contains(text(),'✖ Clear all filters')]")
        for page_number in range(1, 10):
            self.click_element(f'//p[1]//a[{page_number}]')

        # Search for 'sohel', click on a row header, and view history
        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("sohel")
        self.click_element("//input[@value='Search']")
        self.click_element(
            "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/table[1]/tbody[1]/tr[1]/th[1]/a[1]")
        self.click_element("//a[@class='historylink']")

        # Navigate back to 'Wallet Historys' and add a new wallet history
        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='Wallet Historys']")
        self.click_element("//a[normalize-space()='Add Wallet History']")
        self.click_element("//a[@href='/admin/txnms/wallethistory/add/'][normalize-space()='Add']")

        # Navigate back to 'Wallet Historys' and logout
        self.click_element("//div[@class='breadcrumbs']//a[normalize-space()='Wallet Historys']")
        self.logout()

    def test_switch(self):
        self.groups_XPATH()
        self.cs_model_XPATH()
        self.csms_XPATH()
        self.firmware_version_XPATH()
        self.sites_XPATH()
        self.ticket_XPATH()
        self.users_XPATH()
        self.txnms_XPATH()
        self.wallet_history_XPATH()


admin = AdminPanel()
admin.test_switch()
