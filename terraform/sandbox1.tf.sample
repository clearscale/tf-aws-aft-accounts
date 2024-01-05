module "Sandbox1" {
  source = "./modules/aft-account-request"

  control_tower_parameters = {
    AccountEmail = "aws+sandbox1d@customer.com"
    AccountName  = "Sandbox1"

    ManagedOrganizationalUnit = "Sandbox"

    SSOUserEmail     = "aws+sandbox1d@customer.com"
    SSOUserFirstName = "Sandbox"
    SSOUserLastName  = "nonprod"
  }

  account_tags = {
    "Purpose"     = "AFT shared services"
    "Department"  = "Engineering"
    "Cost Center" = "US"
  }

  change_management_parameters = {
    change_requested_by = "John Doe"
    change_reason       = "testing the account vending process"
  }

  custom_fields = {
    custom1 = "a"
    custom2 = "b"
  }

  account_customizations_name = "sandbox-customizations"
}