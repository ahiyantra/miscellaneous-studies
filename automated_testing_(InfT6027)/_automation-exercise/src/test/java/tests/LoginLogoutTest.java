package tests;

import org.openqa.selenium.By;
import org.testng.Assert;
import org.testng.annotations.Test;
import pages.BasePage;

import java.time.Duration;
import java.util.List;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class LoginLogoutTest extends BaseTest {

    @Test(priority = 1)
    public void testCompleteFlow() {
        BasePage basePage = new BasePage(driver);

        // Step : Handle Consent Overlay
        basePage.handleConsentOverlay();

        // Step : Print alt texts for images to demonstrate locators
        printValuesUsingLocators();

        // Step : Login
        login();

        // Step : Check contact details
        contactDetailsCheck();

        // Step : Wait a second before the end
        BasePage.pause();
    }

    private void login() {
        driver.get("https://www.automationexercise.com/login");

        // Expected page title
        String expectedTitle = "Automation Exercise - Signup / Login";

        // Get the actual page title
        String actualTitle = driver.getTitle();

        // Assert the title matches
        Assert.assertEquals(actualTitle, expectedTitle, "Page title does not match!");

        BasePage.pause();

        // Enter login credentials
        driver.findElement(By.cssSelector("input[data-qa='login-email']")).sendKeys("[information redacted]");
        driver.findElement(By.cssSelector("input[data-qa='login-password']")).sendKeys("[information redacted]");

        BasePage.pause();

        driver.findElement(By.cssSelector("button[data-qa='login-button']")).click();

        // Wait for the page to load
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(1));
        // check for the login confirmation
        WebElement loggedInMessage = driver.findElement(By.xpath("//*[contains(text(), 'TestUser')]"));
        Assert.assertTrue(loggedInMessage.isDisplayed(), "Login verification failed!");
    }

    private void contactDetailsCheck() {
        driver.get("https://automationexercise.com/contact_us");

        // Wait for the page to load
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(1));

        // Logout
        WebElement logoutLink = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")));
        logoutLink.click();

        // Validate successful logout by checking the URL or presence of login link
        Assert.assertTrue(driver.getCurrentUrl().contains("/login"), "Logout failed!");

    }

    public void printValuesUsingLocators() {
        // Locate all image elements using tagName
        List<WebElement> imagesByTag = driver.findElements(By.tagName("img"));
        System.out.println("\nAlt texts for images using tagName:\n");
        for (WebElement img : imagesByTag) {
            System.out.println(img.getAttribute("alt"));
        }

        // Locate specific image using className if applicable
        List<WebElement> imagesByClass = driver.findElements(By.className("girl"));
        System.out.println("\nAlt texts for images using className:\n");
        for (WebElement img : imagesByClass) {
            System.out.println(img.getAttribute("alt"));
        }

        // Locate specific image using name if applicable
        // Assuming `name` attribute exists for any image (no instances in current HTML provided)
        List<WebElement> elementByName = driver.findElements(By.name("csrfmiddlewaretoken"));
        System.out.println("\nHidden values for input using name:\n");
        for (WebElement xyz : elementByName) {
            System.out.println(xyz.getAttribute("value"));
        }
        System.out.println("\n");
    }

}
