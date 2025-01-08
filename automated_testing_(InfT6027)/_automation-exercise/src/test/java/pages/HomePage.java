package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class HomePage {
    WebDriver driver;

    // Constructor
    public HomePage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    // Page Elements
    @FindBy(xpath = "//a[contains(text(),'Signup / Login')]")
    WebElement signupLoginLink;

    @FindBy(xpath = "//a[contains(text(),'Contact us')]")
    WebElement contactUsLink;

    @FindBy(xpath = "//a[contains(text(),'Test Cases')]")
    WebElement testCasesLink;

    // Page Actions
    public void clickSignupLogin() {
        signupLoginLink.click();
    }

    public void clickContactUs() {
        contactUsLink.click();
    }

    public void clickTestCases() {
        testCasesLink.click();
    }
}
