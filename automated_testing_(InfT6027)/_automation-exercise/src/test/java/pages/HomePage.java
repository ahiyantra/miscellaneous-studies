package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class HomePage extends BasePage {
    @FindBy(xpath = "//a[contains(text(),'Signup / Login')]")
    WebElement signupLoginLink;

    @FindBy(xpath = "//a[contains(text(),'Contact us')]")
    WebElement contactUsLink;

    @FindBy(xpath = "//a[contains(text(),'Test Cases')]")
    WebElement testCasesLink;

    public HomePage(WebDriver driver) {
        super(driver);
    }

    public void clickSignupLogin() {
        handleConsentOverlay();
        waitAndClick(signupLoginLink);
    }

    public void clickContactUs() {
        handleConsentOverlay();
        waitAndClick(contactUsLink);
    }

    public void clickTestCases() {
        handleConsentOverlay();
        waitAndClick(testCasesLink);
    }
}