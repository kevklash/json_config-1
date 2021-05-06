def serveData():
  """ Defining the default values for the backend config file """
  data = []
  json_data = [
    {
        "id": "title",
        "value": "Mailbox Management Tool"
    },
    {
        "id": "description",
        "value": "This tool is intended to provide details about a customer’s mailbox for query and research purposes only, as well as assist with some login issues. It can provide insights regarding the status of the account, aliases, security mechanisms in use, and mailbox usage, including the potential use of third party applications (POP/IMAP). To address sign in issues, you can also remove all recovery information for users who have never been able to sign in, reset sign in cookies for users and unsuspend users."
    },
    {
        "id": "input_label",
        "value": "Enter the email address you wish to search for:"
    },
    {
        "id": "input_placeholder",
        "value": "Enter email address..."
    },
    {
        "id": "search_button",
        "value": "Search"
    },
    {
        "id": "not_found_confirm",
        "value": "User not found"
    },
    {
        "id": "not_found_info",
        "value": "Couldn't find any active users with this email address in TELUS email powered by Google"
    },
    {
        "id": "not_telus_confirm",
        "value": "Not a valid input"
    },
    {
        "id": "not_telus_info",
        "value": "Please include a valid Telus domain"
    },
    {
        "id": "error_confirm",
        "value": "Server error"
    },
    {
        "id": "error_info",
        "value": "Server appears to be down"
    },
    {
        "id": "header_1",
        "value": "Google account information"
    },
    {
        "id": "rec_email_none",
        "value": "None"
    },
    {
        "id": "rec_phone_none",
        "value": "None"
    },
    {
        "id": "login_time",
        "value": "at"
    },
    {
        "id": "login_time_none",
        "value": "Never signed in"
    },
    {
        "id": "two_step",
        "value": "YES"
    },
    {
        "id": "two_step_no",
        "value": "NO"
    },
    {
        "id": "two_step_tip",
        "value": "Click here to learn more about 2-Step Verification"
    },
    {
        "id": "suspended",
        "value": "YES"
    },
    {
        "id": "not_suspended",
        "value": "NO"
    },
    {
        "id": "header_2",
        "value": "Actions"
    },
    {
        "id": "warning_1",
        "value": "Be mindful that these actions will directly affect the customer's account. Please, use with caution."
    },
    {
        "id": "warning_2",
        "value": "No suspension warnings."
    },
    {
        "id": "warning_3",
        "value": "WARNING: The suspension reason indicates that this user might be suspended due to billing reasons. Unsuspending will not solve the issue until billing is fixed. Please confirm this information before unsuspending."
    },
    {
        "id": "confirm_button",
        "value": "OK"
    },
    {
        "id": "yes_button",
        "value": "Yes"
    },
    {
        "id": "no_button",
        "value": "Cancel"
    },
    {
        "id": "unsuspend_button",
        "value": "UNSUSPEND USER"
    },
    {
        "id": "unsuspend_on",
        "value": "Unsuspend user"
    },
    {
        "id": "unsuspend_off",
        "value": "Since the user is not suspended, this button is disabled"
    },
    {
        "id": "unsuspend_confirm",
        "value": "Unsuspend user?"
    },
    {
        "id": "unsuspend_info",
        "value": "You are about to override this user’s suspension status. This will reactivate the account in the backend."
    },
    {
        "id": "unsuspend_success",
        "value": "The user was successfully unsuspended"
    },
    {
        "id": "cancel_confirm",
        "value": "Cancel"
    },
    {
        "id": "cancel_info",
        "value": "No changes made"
    },
    {
        "id": "recovery_button",
        "value": "REMOVE RECOVERY INFO"
    },
    {
        "id": "recovery_on",
        "value": "Remove recovery info"
    },
    {
        "id": "recovery_off",
        "value": "Since this user has no recovery info, this button is disabled"
    },
    {
        "id": "recovery_confirm",
        "value": "Remove Recovery Info?"
    },
    {
        "id": "recovery_info",
        "value": "This will remove both the recovery email and recovery phone number in the account. If being asked to verify their identity at this time, it will cause them to be asked for a mobile number to receive a code. Otherwise, they will have to update their recovery details on myaccount.google.com to avoid issues in the future."
    },
    {
        "id": "recovery_success",
        "value": "Recovery information has been removed successfully"
    },
    {
        "id": "cookies_button",
        "value": "RESET SIGN-IN COOKIES"
    },
    {
        "id": "cookies_confirm",
        "value": "Reset Sign-In Cookies?"
    },
    {
        "id": "cookies_info",
        "value": "This action will force the user to sign out of all of their active sessions. Doing so requires them to enter their username and password to sign back in to their account."
    },
    {
        "id": "cookies_success",
        "value": "Cookies have been reset successfully"
    },
    {
        "id": "header_3",
        "value": "Changed by"
    },
    {
        "id": "header_4",
        "value": "Affected email"
    },
    {
        "id": "header_5",
        "value": "Event"
    },
    {
        "id": "header_6",
        "value": "Date"
    },
    {
        "id": "header_7",
        "value": "IP"
    },
    {
        "id": "header_8",
        "value": "Self?"
    }
  ]

  for item in range(len(json_data)):
    new_item = json_data[item]
    data.append(new_item) 

  return data