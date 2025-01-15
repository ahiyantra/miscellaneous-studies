package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class ProductCatalogPage extends BasePage {

    private By searchBar = By.id("search_product");
    private By searchButton = By.id("submit_search");
    private By productResult = By.xpath("//p[contains(text(), 'Men Tshirt')]");
    private By addToCartButton = By.xpath("//a[contains(@data-product-id, '2')]");
    private By successPopup = By.id("cartModal");

    public ProductCatalogPage(WebDriver driver) {
        super(driver);
    }

    public void searchForProduct(String productName) {
        handleConsentOverlay();
        driver.findElement(searchBar).sendKeys(productName);
        driver.findElement(searchButton).click();
    }

    public boolean isProductDisplayed() {
        return driver.findElement(productResult).isDisplayed();
    }

    public void addToCart() {
        driver.findElement(addToCartButton).click();
    }

    public boolean isProductAddedToCart() {
        return driver.findElement(successPopup).isDisplayed();
    }
}
