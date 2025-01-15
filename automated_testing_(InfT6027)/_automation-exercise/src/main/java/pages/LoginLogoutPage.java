package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginLogoutPage extends BasePage {

    private By emailField = By.cssSelector("input[data-qa='login-email']");
    private By passwordField = By.cssSelector("input[data-qa='login-password']");
    private By loginButton = By.cssSelector("button[data-qa='login-button']");
    private By loggedInAs = By.xpath("//li[contains(text(), 'Logged in as')]");
    private By logoutButton = By.cssSelector("a[href='/logout']");

    public LoginLogoutPage(WebDriver driver) {
        super(driver);
    }

    public void login(String email, String password) {
        handleConsentOverlay();
        driver.findElement(emailField).sendKeys(email);
        driver.findElement(passwordField).sendKeys(password);
        driver.findElement(loginButton).click();
    }

    public boolean isLoggedIn() {
        return driver.findElement(loggedInAs).isDisplayed() && driver.findElement(logoutButton).isDisplayed();
    }
}
