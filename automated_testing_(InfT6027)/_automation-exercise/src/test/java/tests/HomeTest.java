package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import pages.HomePage;

public class HomeTest extends BaseTest {
    private HomePage homePage;

    @Test(description = "Verify navigation to Signup/Login page")
    public void testNavigateToSignupLogin() {
        homePage = new HomePage(driver);
        homePage.clickSignupLogin();
        // Adding a time delay of 3 seconds before making the assertion
        try {
            Thread.sleep(3000); // 3 seconds delay
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        Assert.assertEquals(driver.getTitle(), "Automation Exercise - Signup / Login");
    }

    @Test(description = "Verify navigation to Contact Us page")
    public void testNavigateToContactUs() {
        homePage = new HomePage(driver);
        homePage.clickContactUs();
        // Adding a time delay of 3 seconds before making the assertion
        try {
            Thread.sleep(3000); // 3 seconds delay
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        Assert.assertEquals(driver.getTitle(), "Automation Exercise - Contact Us");
    }

    @Test(description = "Verify navigation to Test Cases page")
    public void testNavigateToTestCases() {
        homePage = new HomePage(driver);
        homePage.clickTestCases();
        // Adding a time delay of 3 seconds before making the assertion
        try {
            Thread.sleep(3000); // 3 seconds delay
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        Assert.assertEquals(driver.getTitle(), "Automation Practice Website for UI Testing - Test Cases");
    }
}