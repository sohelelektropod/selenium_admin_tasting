
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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

        ticket_pod_or_gun = self.driver.find_element(By.XPATH, "//a[@title='Charging Pod or a socket/gun related issue']")
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
        time.sleep(4)

        txn_ongoing_txn = self.driver.find_element(By.XPATH, "//a[@title='All']")
        txn_ongoing_txn.click()

        txn_yes = self.driver.find_element(By.XPATH, "//a[@title='Yes']")
        txn_yes.click()

        txn_no = self.driver.find_element(By.XPATH, "//a[@title='No']")
        txn_no.click()

        txn_cs_site = self.driver.find_element(By.XPATH, "//ul[@class='admin-filter-CSSite']//select[@class='form-control']")
        txn_cs_site.click()


admin = AdminPanel()
admin.users_XPATH()
admin.ticket_XPATH()
admin.txnms_XPATH()
