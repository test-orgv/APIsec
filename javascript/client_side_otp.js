// VULNERABLE CODE - Client-side validation only
function processTransaction() {
    const otpEntered = document.getElementById('otp').value;
    const otpSent = localStorage.getItem('expectedOtp');
    if (otpEntered === otpSent) {
        executeGoldSale(); // Hacker can call this directly
    }
}