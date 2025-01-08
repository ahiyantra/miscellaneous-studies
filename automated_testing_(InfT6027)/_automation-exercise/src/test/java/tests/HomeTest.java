package tests;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.opera.OperaDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import org.testng.annotations.Parameters;
import pages.HomePage;

public class HomeTest {
    WebDriver driver;
    HomePage homePage;

    @Parameters("browser")
    @BeforeMethod
    public void setUp(String browser) {
        // Set up Firefox or Opera WebDriver based on the browser parameter
        if (browser.equalsIgnoreCase("firefox")) {
            WebDriverManager.firefoxdriver().setup(); // Set up FirefoxDriver using WebDriverManager
            driver = new FirefoxDriver();
        } else if (browser.equalsIgnoreCase("opera")) {
            WebDriverManager.operadriver().setup(); // Set up OperaDriver using WebDriverManager
            driver = new OperaDriver();
        }

        // Maximize the window and navigate to the site
        driver.manage().window().maximize();
        driver.get("https://www.automationexercise.com/");
        homePage = new HomePage(driver);
    }

    @Test(description = "Verify navigation to Signup/Login page")
    public void testNavigateToSignupLogin() {
        homePage.clickSignupLogin();
        Assert.assertEquals(driver.getTitle(), "Automation Exercise - Signup / Login");
    }

    @Test(description = "Verify navigation to Contact Us page")
    public void testNavigateToContactUs() {
        homePage.clickContactUs();
        Assert.assertEquals(driver.getTitle(), "Automation Exercise - Contact Us");
    }

    @Test(description = "Verify navigation to Test Cases page")
    public void testNavigateToTestCases() {
        homePage.clickTestCases();
        Assert.assertEquals(driver.getTitle(), "Automation Exercise - Test Cases");
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
