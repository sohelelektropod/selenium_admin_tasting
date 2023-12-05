import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AdminPanel():

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

        users_clear_all_filters = self.driver.find_element(By.XPATH, "//a[contains(text(),'✖ Clear all filters')]")
        users_clear_all_filters.click()

        for page_number in range(1, 5):
            self.driver.find_element(By.XPATH, f'//p[1]//a[{page_number}]').click()

        users_show_all = self.driver.find_element(By.XPATH, "  //p[1]//a[5]  ")
        users_show_all.click()

        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("sohel")
        users_search = self.driver.find_element(By.XPATH, "//input[@value='Search']")
        users_search.click()

        users_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='mullasohelvajir@gmail.com']")
        users_view.click()

        users_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        users_history.click()

        users_back = self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Users']")
        users_back.click()

        users_add = self.driver.find_element(By.XPATH, "//a[normalize-space()='Add user']")
        users_add.click()

        users_add_from_sidebar = self.driver.find_element(By.XPATH, "//a[@href='/admin/custms/user/add/']")
        users_add_from_sidebar.click()

        users_home = self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Users']")
        users_home.click()

        time.sleep(4)
        self.driver.maximize_window()

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

        ticket_clear_all_filter = self.driver.find_element(By.XPATH, "//a[contains(text(),'✖ Clear all filters')]")
        ticket_clear_all_filter.click()

        for page_number in range(1, 8):
            self.driver.find_element(By.XPATH, f'//p[1]//a[{page_number}]').click()

        ticket_show_all = self.driver.find_element(By.XPATH, "//p[1]//a[9]")
        ticket_show_all.click()

        ticket_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='hjghjghj']")
        ticket_view.click()

        ticket_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        ticket_history.click()

        ticket_back = self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Tickets']")
        ticket_back.click()

        ticket_add = self.driver.find_element(By.XPATH, "//a[normalize-space()='Add ticket']")
        ticket_add.click()

        ticket_add_from_sidebar = self.driver.find_element(By.XPATH, "//a[@href='/admin/custms/ticket/add/']")
        ticket_add_from_sidebar.click()

        ticket_home = self.driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Tickets']")
        ticket_home.click()

        time.sleep(5)

    def txnms_XPATH(self):

        txn_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/admin/txnms/transaction/']")
        txn_link.click()

        txn_ongoing_txn = self.driver.find_element(By.XPATH, "//a[@title='All']")
        txn_ongoing_txn.click()

        txn_yes = self.driver.find_element(By.XPATH, "//a[@title='Yes']")
        txn_yes.click()

        txn_no = self.driver.find_element(By.XPATH, "//a[@title='No']")
        txn_no.click()

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

        txn_no = self.driver.find_element(By.XPATH, "//a[@title='Any date']")
        txn_no.click()

        txn_no = self.driver.find_element(By.XPATH, "//a[@title='Today']")
        txn_no.click()

        txn_no = self.driver.find_element(By.XPATH, "//a[@title='Past 7 days']")
        txn_no.click()

        txn_no = self.driver.find_element(By.XPATH, "//a[@title='This month']")
        txn_no.click()

        txn_no = self.driver.find_element(By.XPATH, "//a[@title='This year']")
        txn_no.click()

        txn_no = self.driver.find_element(By.XPATH, "//a[@title='No date']")
        txn_no.click()

        txn_no = self.driver.find_element(By.XPATH, "//a[@title='Has date']")
        txn_no.click()

        txn_clear_all_filters = self.driver.find_element(By.XPATH, "//a[contains(text(),'✖ Clear all filters')]")
        txn_clear_all_filters.click()

        for page_number in range(1, 9):
            self.driver.find_element(By.XPATH, f'//p[1]//a[{page_number}]').click()

        self.driver.find_element(By.XPATH, "//input[@id='searchbar']").send_keys("sohel")
        txn_search = self.driver.find_element(By.XPATH, "//input[@value='Search']")
        txn_search.click()

        txn_view = self.driver.find_element(By.XPATH, "//a[normalize-space()='e6fe656d-8905-2bd6-62be-4dc1af359394']")
        txn_view.click()

        txn_history = self.driver.find_element(By.XPATH, "//a[@class='historylink']")
        txn_history.click()

        txn_back = self.driver.find_element(By.XPATH,
                                            "//div[@class='breadcrumbs']//a[normalize-space()='Transactions']")
        txn_back.click()

        txn_report = self.driver.find_element(By.XPATH, "//a[@class='reportlink']")
        txn_report.click()

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

        time.sleep(4)

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

        wallet_view = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/table[1]/tbody[1]/tr[1]/th[1]/a[1]")
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
        time.sleep(2)

    def cs_model_XPATH(self):

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

        # self.driver.find_element(By.XPATH, "//input[@id='id_name']").send_keys("2W-1")
        # time.sleep(2)
        #
        # self.driver.find_element(By.XPATH, "//input[@id='id_evse_count']").send_keys("2")
        # time.sleep(2)
        #
        # connector_type = self.driver.find_element(By.XPATH, "//select[@id='id_connector_type']")
        # select = Select(connector_type)
        # select.select_by_visible_text("3-pin Plug")
        # time.sleep(2)
        #
        # self.driver.find_element(By.XPATH, "//input[@id='id_max_output']").send_keys("4")
        # time.sleep(2)
        #
        # save = self.driver.find_element(By.XPATH, "//input[@name='_save']")
        # save.click()

    def sites_XPATH(self):

        siteslink = self.driver.find_element(By.CSS_SELECTOR, "a[href='/admin/csms/site/']")
        siteslink.click()
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

        # self.driver.find_element(By.XPATH, "//input[@id='id_name']").send_keys("testing_site_selenium")
        # time.sleep(2)
        #
        # self.driver.find_element(By.XPATH, "//input[@id='id_evse_count']").send_keys("2")
        # time.sleep(2)
        #
        # site_status_dropdown = self.driver.find_element(By.XPATH, "//select[@id='id_site_status']")
        # select = Select(site_status_dropdown)
        # select.select_by_visible_text("Upcoming")
        # time.sleep(2)
        #
        # self.driver.find_element(By.XPATH, "//input[@id='id_site_contact']").send_keys("9420053193")
        # time.sleep(2)
        #
        # self.driver.find_element(By.XPATH, "//input[@id='id_site_address']").send_keys("Bengaluru")
        # time.sleep(2)
        #
        # state_dropdown = self.driver.find_element(By.XPATH, "//select[@id='id_site_state']")
        # select = Select(state_dropdown)
        # select.select_by_visible_text("Karnataka")
        # time.sleep(2)
        #
        # save = self.driver.find_element(By.XPATH, "//input[@name='_save']")
        # save.click()


admin = AdminPanel()
admin.users_XPATH()
admin.ticket_XPATH()
admin.txnms_XPATH()
admin.wallet_history_XPATH()
admin.cs_model_XPATH()
admin.sites_XPATH()
