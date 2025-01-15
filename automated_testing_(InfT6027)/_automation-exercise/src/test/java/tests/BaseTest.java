package tests;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
//import org.openqa.selenium.opera.OperaDriver;
//import org.openqa.selenium.chrome.ChromeDriver;
//import org.openqa.selenium.chrome.ChromeOptions;
//import org.openqa.selenium.opera.OperaOptions;
//import org.openqa.selenium.edge.EdgeDriver;
//import org.openqa.selenium.edge.EdgeOptions;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.ie.InternetExplorerOptions;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Parameters;

import java.io.File;

public class BaseTest {
    protected WebDriver driver;

    @BeforeMethod
    @Parameters("browser")
    public void setUp(String browser) {
        switch (browser.toLowerCase()) {
            case "firefox":
                WebDriverManager.firefoxdriver().setup();

                // Firefox-specific options
                FirefoxOptions firefoxOptions = new FirefoxOptions();

                // Considered using a headless setup because the website had too many unexpected ad popups interrupting interactions
                //firefoxOptions.addArguments("--headless");

                // Add uBlock Origin extension for ad blocking
                File firefoxExtension = new File("E:\\_LBTU-LLU_\\03rd-semester\\InfT6027 _ automated testing (automatizētā testēšana)\\03rd-assignment-work\\used_softwares\\firefox-ublock\\uBlock0_1.62.0.firefox.xpi");
                firefoxOptions.addPreference("xpinstall.signatures.required", false);
                firefoxOptions.addPreference("extensions.install.requireSecureOrigin", false);
                firefoxOptions.addPreference("extensions.autoDisableScopes", 0);
                firefoxOptions.addPreference("extensions.enabledScopes", 15);
                firefoxOptions.addArguments("--install-extension=" + firefoxExtension.getAbsolutePath());

                // Disable telemetry and update checks
                firefoxOptions.addPreference("browser.tabs.warnOnClose", false);
                firefoxOptions.addPreference("datareporting.policy.dataSubmissionEnabled", false);
                firefoxOptions.addPreference("app.update.auto", false);

                // Ignore TLS certificate errors
                firefoxOptions.setAcceptInsecureCerts(true);

                driver = new FirefoxDriver(firefoxOptions);
                break;
            /*
            case "internetexplorer":
                WebDriverManager.iedriver().setup(); // Automatically install correct IE driver
                InternetExplorerOptions ieOptions = new InternetExplorerOptions();
                ieOptions.introduceFlakinessByIgnoringSecurityDomains(); // Required for IE
                ieOptions.ignoreZoomSettings(); // Ignore zoom level settings
                ieOptions.setCapability("nativeEvents", false); // Disable native events to avoid issues
                ieOptions.setCapability("ignoreProtectedModeSettings", true); // Required for IE
                ieOptions.setCapability("requireWindowFocus", true); // To ensure stable automation
                driver = new InternetExplorerDriver(ieOptions);
                break;
            */
            default:
                throw new IllegalArgumentException("Unsupported browser: " + browser);
        }

        driver.manage().window().maximize();
        driver.get("https://www.automationexercise.com");
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
