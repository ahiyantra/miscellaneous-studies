package tests;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.opera.OperaDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Parameters;

import java.time.Duration;

public class BaseTest {
    protected WebDriver driver;

    @Parameters("browser")
    @BeforeMethod
    public void setUp(String browser) {
        System.out.println("!!! WebDriverManager.chromedriver().getDownloadedDriverVersion() = " + WebDriverManager.chromedriver().getDownloadedDriverVersion());
        if (browser.equalsIgnoreCase("firefox")) {
            WebDriverManager.firefoxdriver().setup();  // Set up Firefox driver
            driver = new FirefoxDriver();
        } else if (browser.equalsIgnoreCase("opera")) {
            WebDriverManager.operadriver().setup();  // Set up Opera driver
            driver = new OperaDriver();
        }
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.manage().window().maximize();
        driver.get("https://automationexercise.com");
        System.out.println("!!! WebDriverManager.chromedriver().getDownloadedDriverVersion() = " + WebDriverManager.chromedriver().getDownloadedDriverVersion());
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
