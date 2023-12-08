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
        button = self.driver.find_element(By.CSS_SELECTOR, 'input[value="Log in"]')
        button.click()

    def users_XPATH(self):

        self.login()

        users_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/admin/custms/user/']")
        users_link.click()

        changelist_element = self.driver.find_element(By.ID, 'changelist')

        relative_xpath = ".//ul[1]//li[1]//a[1]"
        users_all_cso = changelist_element.find_element(By.XPATH, relative_xpath)
        users_all_cso.click()

        users_yes_cso = self.driver.find_element(By.XPATH, "//ul[1]//li[2]//a[1]")
        users_yes_cso.click()

        users_no_cso = self.driver.find_element(By.XPATH, "//ul[1]//li[3]//a[1]")
        users_no_cso.click()

        users_all_staff = self.driver.find_element(By.XPATH, "//ul[2]//li[1]//a[1]")
        users_all_staff.click()

        users_yes_staff = self.driver.find_element(By.XPATH, "//ul[2]//li[2]//a[1]")
        users_yes_staff.click()

        users_no_staff = self.driver.find_element(By.XPATH, "//ul[2]//li[3]//a[1]")
        users_no_staff.click()

        users_all_superuser = self.driver.find_element(By.XPATH, "//ul[3]//li[1]//a[1]")
        users_all_superuser.click()

        users_yes_superuser = self.driver.find_element(By.XPATH, "//ul[3]//li[2]//a[1]")
        users_yes_superuser.click()

        users_no_superuser = self.driver.find_element(By.XPATH, "//ul[3]//li[3]//a[1]")
        users_no_superuser.click()

        users_all_active = self.driver.find_element(By.XPATH, "//ul[4]//li[1]//a[1]")
        users_all_active.click()

        users_yes_active = self.driver.find_element(By.XPATH, "//ul[4]//li[2]//a[1]")
        users_yes_active.click()

        users_no_active = self.driver.find_element(By.XPATH, "//ul[5]//li[1]//a[1]")
        users_no_active.click()

        users_groups = self.driver.find_element(By.XPATH, "//a[@title='customer service']")
        users_groups.click()
        time.sleep(5)

        users_clear_all_filters = self.driver.find_element(By.XPATH, "//a[contains(text(),'✖ Clear all filters')]")
        users_clear_all_filters.click()
        time.sleep(2)

        for page_number in range(1, 5):
            self.driver.find_element(By.XPATH, f'//p[1]//a[{page_number}]').click()

        users_show_all = self.driver.find_element(By.XPATH, "  //p[1]//a[5]  ")
        users_show_all.click()

        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("sohel")
        users_search = self.driver.find_element(By.XPATH, "//input[@value='Search']")
        users_search.click()
        time.sleep(2)

        users_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='mullasohelvajir@gmail.com']")
        users_view.click()
        time.sleep(2)

        users_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        users_history.click()
        time.sleep(2)

        users_back = self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Users']")
        users_back.click()

        users_add = self.driver.find_element(By.XPATH, "//a[normalize-space()='Add user']")
        users_add.click()
        time.sleep(2)

        users_add_from_sidebar = self.driver.find_element(By.XPATH, "//a[@href='/admin/custms/user/add/']")
        users_add_from_sidebar.click()
        time.sleep(2)

        users_home = self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Users']")
        users_home.click()

        time.sleep(10)

    def ticket_XPATH(self):

        ticket_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/admin/custms/ticket/']")
        ticket_link.click()

        ticket_pod_or_gun = self.driver.find_element(By.XPATH,
                                                     "//a[@title='Charging Pod or a socket/gun related issue']")
        ticket_pod_or_gun.click()

        ticket_rfid = self.driver.find_element(By.XPATH, "//a[@title='RFID Card related issue']")
        ticket_rfid.click()

        ticket_billing_or_payment = self.driver.find_element(By.XPATH, "//a[@title='Billing or payment related issue']")
        ticket_billing_or_payment.click()

        ticket_app = self.driver.find_element(By.XPATH, "//a[@title='Mobile App related issue']")
        ticket_app.click()

        ticket_other = self.driver.find_element(By.XPATH, "//a[@title='Other issues']")
        ticket_other.click()
        time.sleep(2)

        ticket_clear_all_filter = self.driver.find_element(By.XPATH, "//a[contains(text(),'✖ Clear all filters')]")
        ticket_clear_all_filter.click()
        time.sleep(2)

        for page_number in range(1, 8):
            self.driver.find_element(By.XPATH, f'//p[1]//a[{page_number}]').click()

        ticket_show_all = self.driver.find_element(By.XPATH, "//p[1]//a[9]")
        ticket_show_all.click()
        time.sleep(2)

        ticket_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='hjghjghj']")
        ticket_view.click()
        time.sleep(2)

        ticket_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        ticket_history.click()
        time.sleep(2)

        ticket_back = self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Tickets']")
        ticket_back.click()

        ticket_add = self.driver.find_element(By.XPATH, "//a[normalize-space()='Add ticket']")
        ticket_add.click()

        ticket_add_from_sidebar = self.driver.find_element(By.XPATH, "//a[@href='/admin/custms/ticket/add/']")
        ticket_add_from_sidebar.click()
        time.sleep(2)

        ticket_home = self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Tickets']")
        ticket_home.click()

        time.sleep(10)

    def txnms_XPATH(self):

        txn_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/admin/txnms/transaction/']")
        txn_link.click()

        txn_ongoing_txn = self.driver.find_element(By.XPATH, "//a[@title='All']")
        txn_ongoing_txn.click()

        txn_yes = self.driver.find_element(By.XPATH, "//a[@title='Yes']")
        txn_yes.click()

        txn_no = self.driver.find_element(By.XPATH, "//a[@title='No']")
        txn_no.click()
        time.sleep(2)

        site_names = [
            'All', 'Eastwood Layout', 'Surat-Amroli', 'Surat-Nitech',
            'BHive-HSR Layout', 'Vega City-BLR', 'Padmavati Foundry',
            'MANGALAM INTERMEDIATES UNIT 2', 'Eastwood_2CDemo', 'Shraddha Motors -TATA Motors'
        ]

        for site_name in site_names:
            dropdown = self.driver.find_element(By.XPATH,
                                                "//ul[@class='admin-filter-CSSite']//select[@class='form-control']")
            select = Select(dropdown)
            select.select_by_visible_text(site_name)
        time.sleep(2)

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
            dropdown = self.driver.find_element(By.XPATH,
                                                "//ul[@class='admin-filter-chargingstation']//select[@class='form-control']")
            select = Select(dropdown)
            select.select_by_visible_text(charger_name)
        time.sleep(2)

        txn_anydate = self.driver.find_element(By.XPATH, "//a[@title='Any date']")
        txn_anydate.click()

        txn_today = self.driver.find_element(By.XPATH, "//a[@title='Today']")
        txn_today.click()

        txn_past = self.driver.find_element(By.XPATH, "//a[@title='Past 7 days']")
        txn_past.click()

        txn_month = self.driver.find_element(By.XPATH, "//a[@title='This month']")
        txn_month.click()

        txn_year = self.driver.find_element(By.XPATH, "//a[@title='This year']")
        txn_year.click()

        txn_no_date = self.driver.find_element(By.XPATH, "//a[@title='No date']")
        txn_no_date.click()

        txn_has_date = self.driver.find_element(By.XPATH, "//a[@title='Has date']")
        txn_has_date.click()
        time.sleep(2)

        txn_clear_all_filters = self.driver.find_element(By.XPATH, "//a[contains(text(),'✖ Clear all filters')]")
        txn_clear_all_filters.click()
        time.sleep(2)

        for page_number in range(1, 9):
            self.driver.find_element(By.XPATH, f'//p[1]//a[{page_number}]').click()

        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("sohel")
        txn_search = self.driver.find_element(By.XPATH, "//input[@value='Search']")
        txn_search.click()
        time.sleep(2)

        txn_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='e6fe656d-8905-2bd6-62be-4dc1af359394']")
        txn_view.click()
        time.sleep(2)

        txn_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        txn_history.click()
        time.sleep(2)

        txn_back = self.driver.find_element(By.XPATH,
                                            "//div[@class='breadcrumbs']//a[normalize-space()='Transactions']")
        txn_back.click()

        txn_report = self.driver.find_element(By.XPATH, "//a[@class='reportlink']")
        txn_report.click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_start_date']").send_keys("01/12/2022")

        self.driver.find_element(By.XPATH, "//input[@id='id_end_date']").send_keys("01/12/2023")

        site_dropdown = self.driver.find_element(By.XPATH, "//select[@id='id_site']")
        select = Select(site_dropdown)

        select.select_by_visible_text("Eastwood Layout")

        txn_report_submit = self.driver.find_element(By.XPATH, "//input[@value='Submit']")
        txn_report_submit.click()
        time.sleep(4)

        txn_home = self.driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
        txn_home.click()

        txn_sidebar_home = self.driver.find_element(By.XPATH, "//a[normalize-space()='Transactions']")
        txn_sidebar_home.click()

        time.sleep(10)

    def wallet_history_XPATH(self):

        wallet_link = self.driver.find_element(By.CSS_SELECTOR, "tr[class='model-wallethistory'] th[scope='row'] a")
        wallet_link.click()
        time.sleep(2)

        wallet_razorpay_all = self.driver.find_element(By.XPATH, "//div[@id='changelist']//ul[1]//li[1]//a[1]")
        wallet_razorpay_all.click()
        time.sleep(2)

        wallet_razorpay_yes = self.driver.find_element(By.XPATH, "//a[@title='Yes']")
        wallet_razorpay_yes.click()
        time.sleep(2)

        wallet_razorpay_no = self.driver.find_element(By.XPATH, "//a[@title='No']")
        wallet_razorpay_no.click()
        time.sleep(2)

        wallet_record_all = self.driver.find_element(By.XPATH, "//ul[2]//li[1]//a[1]")
        wallet_record_all.click()
        time.sleep(2)

        wallet_record_credit = self.driver.find_element(By.XPATH, "//a[@title='Credit']")
        wallet_record_credit.click()
        time.sleep(2)

        wallet_record_debit = self.driver.find_element(By.XPATH, "//a[@title='Debit']")
        wallet_record_debit.click()
        time.sleep(2)

        wallet_clear_all_filter = self.driver.find_element(By.XPATH, "//a[contains(text(),'✖ Clear all filters')]")
        wallet_clear_all_filter.click()
        time.sleep(2)

        for page_number in range(1, 10):
            self.driver.find_element(By.XPATH, f'//p[1]//a[{page_number}]').click()

        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("sohel")
        wallet_search = self.driver.find_element(By.XPATH, "//input[@value='Search']")
        wallet_search.click()
        time.sleep(2)

        wallet_view = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/table[1]/tbody[1]/tr[1]/th[1]/a[1]")
        wallet_view.click()
        time.sleep(2)

        wallet_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        wallet_history.click()
        time.sleep(2)

        wallet_back = self.driver.find_element(By.XPATH,
                                               "//div[@class='breadcrumbs']//a[normalize-space()='Wallet Historys']")
        wallet_back.click()
        time.sleep(4)

        wallet_add = self.driver.find_element(By.XPATH, "//a[normalize-space()='Add Wallet History']")
        wallet_add.click()
        time.sleep(4)

        wallet_add_from_sidebar = self.driver.find_element(By.XPATH,
                                                           "//a[@href='/admin/txnms/wallethistory/add/'][normalize-space()='Add']")
        wallet_add_from_sidebar.click()
        time.sleep(2)

        wallet_back = self.driver.find_element(By.XPATH,
                                               "//div[@class='breadcrumbs']//a[normalize-space()='Wallet Historys']")
        wallet_back.click()
        time.sleep(10)

    def cs_model_XPATH(self):

        self.login()

        cs_model_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/admin/csms/csmodel/']")
        cs_model_link.click()
        time.sleep(2)

        cs_model_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='30KW CCS2']")
        cs_model_view.click()
        time.sleep(2)

        cs_model_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        cs_model_history.click()
        time.sleep(2)

        cs_model_back = self.driver.find_element(By.XPATH,
                                                 "//div[@class='breadcrumbs']//a[normalize-space()='CS Models']")
        cs_model_back.click()
        time.sleep(2)

        cs_model_add = self.driver.find_element(By.XPATH, "//a[normalize-space()='Add CS Model']")
        cs_model_add.click()
        time.sleep(2)

        cs_model_add_from_sidebar = self.driver.find_element(By.XPATH, "//a[@href='/admin/csms/csmodel/add/']")
        cs_model_add_from_sidebar.click()
        time.sleep(2)

        # ------Add cs_model form test---------

        self.driver.find_element(By.XPATH, "//input[@id='id_name']").send_keys("2W-2")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_evse_count']").clear()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_evse_count']").send_keys("2")
        time.sleep(2)

        connector_type = self.driver.find_element(By.XPATH, "//select[@id='id_connector_type']")
        select = Select(connector_type)
        select.select_by_visible_text("3-pin Plug")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_max_output']").clear()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_max_output']").send_keys("4")
        time.sleep(2)

        save = self.driver.find_element(By.XPATH, "//input[@name='_save']")
        save.click()
        time.sleep(10)

    def sites_XPATH(self):

        sites_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/admin/csms/site/']")
        sites_link.click()
        time.sleep(2)

        sites_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='Shraddha Motors -TATA Motors']")
        sites_view.click()
        time.sleep(2)

        site_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        site_history.click()
        time.sleep(2)

        sites_back = self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Sites']")
        sites_back.click()
        time.sleep(2)

        sites_add = self.driver.find_element(By.XPATH, "//a[normalize-space()='Add site']")
        sites_add.click()
        time.sleep(2)

        sites_add_from_sidebar = self.driver.find_element(By.XPATH,
                                                          "//a[@href='/admin/csms/site/add/'][normalize-space()='Add']")
        sites_add_from_sidebar.click()
        time.sleep(2)

        # ------Add site form test---------

        self.driver.find_element(By.XPATH, "//input[@id='id_name']").send_keys("testing_site_selenium_1")
        time.sleep(2)

        site_status_dropdown = self.driver.find_element(By.XPATH, "//select[@id='id_site_status']")
        select = Select(site_status_dropdown)
        select.select_by_visible_text("Upcoming")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_site_contact']").send_keys("9420053194")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_site_address']").send_keys("Bengaluru")
        time.sleep(2)

        state_dropdown = self.driver.find_element(By.XPATH, "//select[@id='id_site_state']")
        select = Select(state_dropdown)
        select.select_by_visible_text("Karnataka")
        time.sleep(2)

        use_invoice_name_checkbox = self.driver.find_element(By.XPATH, "//input[@id='id_is_owner']")
        use_invoice_name_checkbox.click()

        self.driver.find_element(By.XPATH, "//input[@id='id_invoice_name']").send_keys("sohel mulla one")
        self.driver.find_element(By.XPATH, "//input[@id='id_account_name']").send_keys("sohel mulla one")
        self.driver.find_element(By.XPATH, "//input[@id='id_account_number']").send_keys("1234567891")
        self.driver.find_element(By.XPATH, "//input[@id='id_bank_ifsc']").send_keys("ICICI0000594")

        time.sleep(4)

        save = self.driver.find_element(By.XPATH, "//input[@name='_save']")
        save.click()
        time.sleep(10)

    def csms_XPATH(self):

        csms_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/admin/csms/chargingstation/']")
        csms_link.click()

        site_names = [
            'All', 'Eastwood Layout', 'Surat-Amroli', 'Surat-Nitech',
            'BHive-HSR Layout', 'Vega City-BLR', 'Padmavati Foundry',
            'MANGALAM INTERMEDIATES UNIT 2', 'Eastwood_2CDemo', 'Shraddha Motors -TATA Motors'
        ]

        for site_name in site_names:
            csms_cs_site_filter = self.driver.find_element(By.XPATH, "//select[@class='form-control']")
            select = Select(csms_cs_site_filter)
            select.select_by_visible_text(site_name)

        csms_clear_all_filter = self.driver.find_element(By.XPATH, "//a[contains(text(),'✖ Clear all filters')]")
        csms_clear_all_filter.click()
        time.sleep(2)

        for page_number in range(1,3):
            csms_pagination = self.driver.find_element(By.XPATH, f"//p[1]//a[{page_number}]")
            csms_pagination.click()

        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("Sahil")
        csms_search = self.driver.find_element(By.XPATH, "//input[@value='Search']")
        csms_search.click()
        time.sleep(2)

        csms_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='Sahil']")
        csms_view.click()
        time.sleep(2)

        csms_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        csms_history.click()
        time.sleep(2)

        csms_back_history = self.driver.find_element(By.XPATH, "//a[normalize-space()='Sahil']")
        csms_back_history.click()
        time.sleep(2)

        csms_manage_confg = self.driver.find_element(By.XPATH, "//a[@class='configlink']")
        csms_manage_confg.click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_PlatformCtrlr: Name']").send_keys("TestCharger2")

        csms_manage_confg_submit = self.driver.find_element(By.XPATH, "//input[@value='Submit']")
        csms_manage_confg_submit.click()

        csms_home = self.driver.find_element(By.XPATH, "//a[normalize-space()='Charging Stations']")
        csms_home.click()

        csms_add_from_sidebar = self.driver.find_element(By.XPATH, "//a[@href='/admin/csms/chargingstation/add/']")
        csms_add_from_sidebar.click()
        time.sleep(2)

        csms_home = self.driver.find_element(By.XPATH, "//a[normalize-space()='Charging Stations']")
        csms_home.click()
        time.sleep(2)

        csms_add = self.driver.find_element(By.XPATH, "//a[normalize-space()='Add Charging Station']")
        csms_add.click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_device_id']").send_keys("12345675")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_product_id']").send_keys("test_selenium_5")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='id_name']").send_keys("test_selenium_cs_5")
        time.sleep(2)

        csms_select_cs_model = self.driver.find_element(By.XPATH, "//select[@id='id_cs_model']")
        select = Select(csms_select_cs_model)
        select.select_by_visible_text("2ww")
        time.sleep(2)

        csms_select_firmware_version = self.driver.find_element(By.XPATH, "//select[@id='id_firmware_version']")
        select = Select(csms_select_firmware_version)
        select.select_by_visible_text("2.0.32")
        time.sleep(2)

        csms_select_site = self.driver.find_element(By.XPATH, "//select[@id='id_cs_site']")
        select = Select(csms_select_site)
        select.select_by_visible_text("testing_site_selenium")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//textarea[@id='id_location']").send_keys('{"type":"Point","coordinates":[76.924338,18.052479]}')

        csms_save = self.driver.find_element(By.XPATH, "//input[@name='_save']")
        csms_save.click()
        time.sleep(5)

        csms_force_update = self.driver.find_element(By.XPATH, "//a[@class='configlink']")
        csms_force_update.click()

        csms_force_update_site = self.driver.find_element(By.XPATH, "//select[@id='id_site']")
        select = Select(csms_force_update_site)
        select.select_by_visible_text("testing_site_selenium")

        csms_force_update_cs = self.driver.find_element(By.XPATH, "//option[normalize-space()='testing_selenium_cs']")
        csms_force_update_cs.click()

        csms_force_update_submit = self.driver.find_element(By.XPATH, "//input[@value='Submit']")
        csms_force_update_submit.click()
        time.sleep(4)

        csms_home = self.driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
        csms_home.click()

        csms_home = self.driver.find_element(By.XPATH, "//a[normalize-space()='Charging Stations']")
        csms_home.click()
        time.sleep(10)

    def firmware_version_XPATH(self):

        fv_link = self.driver.find_element(By.CSS_SELECTOR, "tr[class='model-firmwareversion'] th[scope='row'] a")
        fv_link.click()

        fv_add = self.driver.find_element(By.XPATH, "//a[normalize-space()='Add Firmware Version']")
        fv_add.click()

        self.driver.find_element(By.XPATH, "//input[@id='id_version_name']").send_keys("selenium_test_2.0")

        fv_add_cs_model_select = self.driver.find_element(By.XPATH, "//select[@id='id_cs_model']")
        select = Select(fv_add_cs_model_select)
        select.select_by_visible_text("2ww")

        fv_remove_null = self.driver.find_element(By.XPATH, "//textarea[@id='id_config']")
        fv_remove_null.clear()
        time.sleep(8)

        self.driver.find_element(By.XPATH, "//textarea[@id='id_config']").send_keys('[{"variable": {"name": "ModelNumber"}, "component": {"name": "PlatformCtrlr"}, "attributeValue": "60KW CCS2", "attributeVarType": "CONFIG_RO", "attributeValueType": "stringType", "attributeFactoryDefValue": "60KW CCS2"}, {"variable": {"name": "FirmwareVersion"}, "component": {"name": "PlatformCtrlr"}, "attributeValue": "3.2.19-2.1.6", "attributeVarType": "CONFIG_RO", "attributeValueType": "stringType", "attributeFactoryDefValue": "3.2.19-2.1.6"}, {"variable": {"name": "Name"}, "component": {"name": "PlatformCtrlr"}, "attributeValue": "TestCharger3", "attributeVarType": "CONFIG_RW", "attributeValueType": "stringType", "attributeFactoryDefValue": "Undefined"}, {"variable": {"name": "Available"}, "component": {"evse": {"id": "1"}, "name": "ChargingStation"}, "attributeValue": "1", "attributeVarType": "CONFIG_RO", "attributeValueType": "boolType", "attributeFactoryDefValue": "1"}, {"variable": {"name": "Available"}, "component": {"evse": {"id": "2"}, "name": "ChargingStation"}, "attributeValue": "1", "attributeVarType": "CONFIG_RO", "attributeValueType": "boolType", "attributeFactoryDefValue": "1"}, {"variable": {"name": "Available"}, "component": {"evse": {"id": "0"}, "name": "ChargingStation"}, "attributeValue": "1", "attributeVarType": "CONFIG_RO", "attributeValueType": "boolType", "attributeFactoryDefValue": "1"}, {"variable": {"name": "AvailabilityState"}, "component": {"name": "ChargingStation"}, "attributeValue": "", "attributeVarType": "STATE_V", "attributeValueType": "stringType", "attributeFactoryDefValue": "Undefined"}, {"variable": {"name": "AvailabilityState"}, "component": {"evse": {"id": "1"}, "name": "ChargingStation"}, "attributeValue": "", "attributeVarType": "STATE_V", "attributeValueType": "stringType", "attributeFactoryDefValue": "Undefined"}, {"variable": {"name": "AvailabilityState"}, "component": {"evse": {"id": "2"}, "name": "ChargingStation"}, "attributeValue": "", "attributeVarType": "STATE_V", "attributeValueType": "stringType", "attributeFactoryDefValue": "Undefined"}, {"variable": {"name": "AvailabilityState"}, "component": {"evse": {"id": "0"}, "name": "ChargingStation"}, "attributeValue": "1", "attributeVarType": "STATE_V", "attributeValueType": "stringType", "attributeFactoryDefValue": "Undefined"}]')

        fv_save = self.driver.find_element(By.XPATH, "//input[@name='_save']")
        fv_save.click()
        time.sleep(4)

        fv_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='selenium_test_1.0']")
        fv_view.click()

        fv_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        fv_history.click()

        fv_home = self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Firmware Versions']")
        fv_home.click()
        time.sleep(10)

    def groups_XPATH(self):

        groups_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/admin/auth/group/']")
        groups_link.click()

        groups_add = self.driver.find_element(By.XPATH,"//a[normalize-space()='Add group']")
        groups_add.click()

        self.driver.find_element(By.XPATH, "//input[@id='id_name']").send_keys("testing service")

        groups_add_permission = self.driver.find_element(By.XPATH, "//option[@title='admin | log entry | Can view log entry']")
        groups_add_permission.click()

        groups_add_choice = self.driver.find_element(By.XPATH, "//a[@id='id_permissions_add_link']")
        groups_add_choice.click()

        groups_add_permission = self.driver.find_element(By.XPATH, "//option[@title='auth | group | Can view group']")
        groups_add_permission.click()

        groups_add_choice = self.driver.find_element(By.XPATH, "//a[@id='id_permissions_add_link']")
        groups_add_choice.click()
        time.sleep(4)

        groups_save = self.driver.find_element(By.XPATH, "//input[@name='_save']")
        groups_save.click()

        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("testing")
        groups_search = self.driver.find_element(By.XPATH, "//input[@value='Search']")
        groups_search.click()
        time.sleep(4)

        groups_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='testing service']")
        groups_view.click()
        time.sleep(5)

        groups_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        groups_history.click()
        time.sleep(5)

        groups_home= self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Groups']")
        groups_home.click()
        time.sleep(10)


admin = AdminPanel()
admin.users_XPATH()
admin.ticket_XPATH()
admin.txnms_XPATH()
admin.wallet_history_XPATH()
admin.cs_model_XPATH()
admin.sites_XPATH()
admin.csms_XPATH()
admin.firmware_version_XPATH()
admin.groups_XPATH()

