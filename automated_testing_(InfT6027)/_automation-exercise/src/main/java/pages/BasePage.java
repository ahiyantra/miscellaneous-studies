package pages;

import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class BasePage {
    protected WebDriver driver;
    protected WebDriverWait wait;
    private static final int DELAY_MILLISECONDS = 1000; // 5-second delay

    public BasePage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    // Pause for a specific duration
    public static void pause() {
        try {
            Thread.sleep(DELAY_MILLISECONDS);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    // Inject JavaScript to block ads dynamically (no delay for this method)
    public void injectAdBlocker() {
        String adBlockScript = """
                var css = document.createElement('style');
                css.type = 'text/css';
                css.innerText = `
                    [id*='ad'], [class*='ad'], iframe, [src*='ad'] {
                        display: none !important;
                    }
                `;
                document.head.appendChild(css);
            """;

        ((JavascriptExecutor) driver).executeScript(adBlockScript);
    }

    // Handle consent overlay if it appears (includes delay)
    public void handleConsentOverlay() {
        try {
            WebElement overlay = driver.findElement(By.className("fc-dialog"));
            if (overlay.isDisplayed()) {
                pause(); // Add a delay before dismissing the overlay
                WebElement consentButton = overlay.findElement(By.className("fc-cta-consent"));
                consentButton.click();
                System.out.println("Consent overlay dismissed.");
                pause(); // Add a delay after dismissing the overlay
            }
        } catch (Exception e) {
            System.out.println("Consent overlay not present.");
        }
    }

}
