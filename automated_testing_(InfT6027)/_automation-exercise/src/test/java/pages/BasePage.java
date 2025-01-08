package pages;

import org.openqa.selenium.*;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class BasePage {
    protected WebDriver driver;
    protected WebDriverWait wait;

    public BasePage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        PageFactory.initElements(driver, this);
    }

    public void handleConsentOverlay() {
        try {
            // Wait for the consent dialog to be present
            WebElement consentButton = wait.until(ExpectedConditions.elementToBeClickable(
                    By.cssSelector("button.fc-button.fc-cta-consent")
            ));

            // Try regular click first
            try {
                consentButton.click();
            } catch (ElementClickInterceptedException e) {
                // If regular click fails, try JavaScript click
                ((JavascriptExecutor) driver).executeScript("arguments[0].click();", consentButton);
            }

            // Wait for overlay to disappear
            wait.until(ExpectedConditions.invisibilityOfElementLocated(
                    By.cssSelector(".fc-dialog-overlay")
            ));
        } catch (TimeoutException | NoSuchElementException e) {
            // If overlay is not present or already handled, continue
            System.out.println("Consent overlay not present or already handled");
        }
    }

    // Wait for the page to be fully loaded (document.readyState is "complete")
    public void ensurePageLoaded() {
        JavascriptExecutor jsExecutor = (JavascriptExecutor) driver;
        wait.until(driver -> jsExecutor.executeScript("return document.readyState").equals("complete"));
    }

    protected void waitAndClick(WebElement element) {
        try {
            wait.until(ExpectedConditions.elementToBeClickable(element));
            element.click();
        } catch (ElementClickInterceptedException e) {
            // If regular click fails, try JavaScript click
            ((JavascriptExecutor) driver).executeScript("arguments[0].click();", element);
        }
    }

    public String getPageTitle() {
        return driver.getTitle();
    }
}
