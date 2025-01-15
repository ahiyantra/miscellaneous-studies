package pages;

import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class ElementClickHelper {

    private WebDriver driver;

    public ElementClickHelper(WebDriver driver) {
        this.driver = driver;
    }

    public void safeClick(By locator) {
        WebElement element = driver.findElement(locator);

        // Scroll element into view
        ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", element);

        // Wait for potential interruptions and hide them
        hideInterruptions();

        // Click the element
        element.click();
    }

    private void hideInterruptions() {
        try {
            // Define potential interrupting elements (ads, overlays, etc.)
            By[] potentialInterruptions = new By[]{
                    By.className("adsbygoogle"), // Example for Google Ads
                    By.className("overlay"),    // Example for overlay classes
                    By.id("popup"),             // Example for a popup ID
                    // Add more locators if necessary
            };

            for (By interruptionLocator : potentialInterruptions) {
                WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(2));
                wait.until(ExpectedConditions.presenceOfAllElementsLocatedBy(interruptionLocator));

                for (WebElement interruption : driver.findElements(interruptionLocator)) {
                    // Hide the interruption element
                    ((JavascriptExecutor) driver).executeScript("arguments[0].style.display='none';", interruption);
                }
            }
        } catch (TimeoutException e) {
            // No interruptions found; proceed
        }
    }
}
