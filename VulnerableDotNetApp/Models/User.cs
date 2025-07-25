namespace VulnerableDotNetApp.Models
{
    public class User
    {
        public int Id { get; set; }
        public string Username { get; set; }
        public string Password { get; set; }  // VULNERABLE: Plaintext password
        public string CreditCard { get; set; } // VULNERABLE: Unencrypted PII
    }
}