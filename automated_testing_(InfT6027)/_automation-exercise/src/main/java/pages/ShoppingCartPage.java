package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class ShoppingCartPage extends BasePage {

    private By cartItemName = By.xpath("//td[contains(text(), 'Men Tshirt')]");
    private By cartItemPrice = By.xpath("//td[contains(text(), 'Rs. 400')]");
    private By cartItemQuantity = By.xpath("//td/input[@value='1']");
    private By proceedToCheckoutButton = By.xpath("//a[contains(text(), 'Proceed to Checkout')]");

    public ShoppingCartPage(WebDriver driver) {
        super(driver);
    }

    public boolean isProductInCart() {
        return driver.findElement(cartItemName).isDisplayed() &&
                driver.findElement(cartItemPrice).isDisplayed() &&
                driver.findElement(cartItemQuantity).isDisplayed();
    }

    public void proceedToCheckout() {
        driver.findElement(proceedToCheckoutButton).click();
    }
}
