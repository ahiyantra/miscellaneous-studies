package tests;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.TimeoutException;
import org.testng.Assert;
import org.testng.annotations.Test;
import pages.BasePage;

import java.time.Duration;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class ShoppingCartTest extends BaseTest {

    @Test(priority = 3)
    public void testCompleteFlow() {
        BasePage basePage = new BasePage(driver);

        // Step : Handle Consent Overlay
        basePage.handleConsentOverlay();

        // Step : Login To Website
        login();

        // Step : Validate Cart
        validateCart();

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

        // Enter login credentials
        driver.findElement(By.cssSelector("input[data-qa='login-email']")).sendKeys("stone.excalibre.99@gmail.com");
        driver.findElement(By.cssSelector("input[data-qa='login-password']")).sendKeys("%exercise~automation%");
        driver.findElement(By.cssSelector("button[data-qa='login-button']")).click();

        // Wait for the page to load
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        WebElement loggedInMessage = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[contains(text(), 'TestUser')]")));
        Assert.assertTrue(loggedInMessage.isDisplayed(), "Login verification failed!");
    }

    private void validateCart() {
        driver.get("https://www.automationexercise.com/view_cart");

        String expectedProductName = "Men Tshirt";
        String expectedProductPrice = "Rs. 400";

        WebElement productNameElement = driver.findElement(By.xpath("/html/body/section/div/div[2]/table/tbody/tr/td[2]/h4/a"));
        String actualProductName = productNameElement.getText();
        Assert.assertEquals(actualProductName, expectedProductName, "Product name does not match!");

        WebElement productPriceElement = driver.findElement(By.xpath("/html/body/section/div/div[2]/table/tbody/tr/td[3]/p"));
        String actualProductPrice = productPriceElement.getText();
        Assert.assertEquals(actualProductPrice, expectedProductPrice, "Product price does not match!");

        // Hide all obstructive elements dynamically
        ((JavascriptExecutor) driver).executeScript(
                "document.querySelectorAll('iframe, div[id^=\"aswift\"], div[class*=\"ads\"]').forEach(el => el.style.display = 'none');");

        // Click the "Proceed to Checkout" button
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        WebElement proceedToCheckoutButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//a[@class='btn btn-default check_out']")));
        proceedToCheckoutButton.click();

        // Validate that the current URL is the checkout page
        Assert.assertTrue(driver.getCurrentUrl().contains("/checkout"), "Failed to proceed to checkout!");

        BasePage.pause();

        // Logout
        WebElement logoutLink = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")));
        logoutLink.click();

        // Validate successful logout
        Assert.assertTrue(driver.getCurrentUrl().contains("/login"), "Logout failed!");
    }
}
