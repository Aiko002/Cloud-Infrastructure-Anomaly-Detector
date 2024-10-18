// Toggle between Sign Up and Sign In forms
function showSignUp() {
    document.getElementById("signUpForm").style.display = "block";
    document.getElementById("signInForm").style.display = "none";
}

function showSignIn() {
    document.getElementById("signUpForm").style.display = "none";
    document.getElementById("signInForm").style.display = "block";
}

// Handle Sign Up Form Submission
document.getElementById("signUpForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Basic validation
    const username = document.getElementById("username").value;
    const email = document.getElementById("signupEmail").value;
    const password = document.getElementById("signupPassword").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
    } else {
        // Redirect to the Sign Up Success Page
        window.location.href = "https://chromewebstore.google.com/category/extensions?pli=1"; // Replace with your actual page URL
    }
});

// Handle Sign In Form Submission
document.getElementById("signInForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Basic validation
    const email = document.getElementById("signinEmail").value;
    const password = document.getElementById("signinPassword").value;

    if (email && password) {
        // Redirect to the Sign In Success Page
        window.location.href = "https://chromewebstore.google.com/category/extensions?pli=1"; // Replace with your actual page URL
    } else {
        alert("Please fill out both fields!");
    }
});
