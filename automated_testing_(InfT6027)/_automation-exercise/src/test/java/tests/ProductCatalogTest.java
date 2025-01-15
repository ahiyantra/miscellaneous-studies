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

import pages.ElementClickHelper;

public class ProductCatalogTest extends BaseTest {

    @Test(priority = 2)
    public void testCompleteFlow() {
        BasePage basePage = new BasePage(driver);

        ElementClickHelper clickHelper = new ElementClickHelper(driver);

        // Step : Handle Consent Overlay
        basePage.handleConsentOverlay();

        // Step : Login To Website
        login();

        // Step : Search for Product and Add to Cart
        searchAndAddToCart(clickHelper);

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
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(1));
        WebElement loggedInMessage = driver.findElement(By.xpath("//*[contains(text(), 'TestUser')]"));
        Assert.assertTrue(loggedInMessage.isDisplayed(), "Login verification failed!");
    }

    private void searchAndAddToCart(ElementClickHelper clickHelper) {
        driver.get("https://www.automationexercise.com/products");

        // Search for the product
        driver.findElement(By.id("search_product")).sendKeys("Men Tshirt");
        driver.findElement(By.id("submit_search")).click();

        // Verify that the searched product is displayed
        Assert.assertTrue(driver.findElement(By.xpath("//p[contains(text(), 'Men Tshirt')]")).isDisplayed(), "Product not found!");


        // create wait variable
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        // Click the "View Product" button
        clickHelper.safeClick(By.xpath("/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a"));

        // Wait for the product details page to load
        wait.until(ExpectedConditions.titleContains("Product Details"));

        // Select the quantity as "2"
        WebElement quantityField = driver.findElement(By.id("quantity"));
        quantityField.clear();
        quantityField.sendKeys("2");

        // Click the "Add to Cart" button
        WebElement addToCartButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button")));
        addToCartButton.click();

        // Wait for the "Added!" popup to appear
        WebElement cartModal = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//div[@class='modal-content']")));
        Assert.assertTrue(cartModal.isDisplayed(), "Add to Cart popup not displayed!");

        BasePage.pause();

        // Click the "Continue Shopping" button
        WebElement continueShoppingButton = driver.findElement(By.xpath("/html/body/section/div/div/div[2]/div[1]/div/div/div[3]/button"));
        continueShoppingButton.click();

        // Ensure the popup disappears
        wait.until(ExpectedConditions.invisibilityOf(cartModal));

        // Proceed to logout
        WebElement logoutLink = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")));
        logoutLink.click();

        // Validate successful logout
        Assert.assertTrue(driver.getCurrentUrl().contains("/login"), "Logout failed!");
    }

}
