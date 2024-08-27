class OrangeHRM_Locators:
    #webpaga locators
    username = "username"
    password = "password"
    submit_button = "//button[@type='submit']"
    profile_image = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img'
    logout_button = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

    # Webpage url
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # excel utilities
    excel_file = "C:\\Users\\sbasi\\Automation\\Zen Queries\\ddtf\\Test_Data\\test_data.xlsx"
    sheet_number = "Sheet1"
    pass_data = "TEST PASS"
    fail_data = "TEST FAILED"