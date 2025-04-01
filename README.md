# My Project Using Portialabs SDK

## Overview

In this project, I built an interactive calculator using the **Portialabs SDK** and **Mistral AI** as the underlying language model provider. The calculator can handle various mathematical queries, including simple arithmetic, square roots, and powers. Users can enter a variety of calculations, and the application processes these using the Portialabs API.

The application was designed to handle rate limits effectively, retrying requests with escalating delays when the rate limit is hit, ensuring smooth user experience even under heavy usage.

## Features
- **Basic Calculations:** Users can ask for simple arithmetic like addition, subtraction, multiplication, and division.
- **Advanced Calculations:** Supports powers and square roots.
- **Rate Limiting:** Handles rate limit errors with retries and delays.
- **Interactive Mode:** Users can continuously enter queries until they type 'quit'.
- **Error Handling:** Graceful error handling with helpful feedback.

## Why I Liked Portialabs API/SDK

1. **Easy Setup & Configuration:**
   The setup with **Portialabs SDK** was straightforward. The `dotenv` integration made it easy to handle API keys and environment variables securely without needing to hardcode them. This setup is clean, efficient, and secure.

2. **Plan Execution Model:**
   One of my favorite features is how Portialabs generates a **plan** for each query before executing it. Instead of just providing a response, it first outlines a structured plan for how to address the question. This makes the interaction feel much more dynamic and controlled, and it provides more flexibility.

3. **Rate Limiting & Retry Logic:**
   Portialabs handles rate limits very efficiently. If the rate limit is exceeded, the system automatically retries the request after a short delay, and this delay increases with each successive retry. This built-in feature saved me a lot of time and effort, as I didn’t have to manually implement my own retry logic.

4. **Error Handling:**
   The error handling was clear and informative. If something went wrong, I received specific error messages that made it easy to troubleshoot. For example, when hitting the rate limit, the message clearly indicated that and helped me adjust my request strategy.

## Things That Didn’t Make Sense or Got Me Stuck

1. **Documentation Was a Bit Sparse in Areas:**
   The documentation is generally helpful, but there were a few spots where I felt it was a bit lacking, particularly around integrating **Mistral AI** with the SDK. It wasn’t immediately obvious how to set things up with this specific language model, so I had to dig around in example code and documentation to piece everything together.

2. **The Plan Output Can Be Overwhelming:**
   The plan generation output can be very detailed (which is good), but at first, I found it a bit overwhelming. The raw output in JSON format can be a lot to handle, especially when you're just trying to focus on the core results. It took me a while to figure out how to parse and display it in a user-friendly way.

3. **Custom Tools Integration Took Some Effort:**
   When I started using **example_tool_registry** to integrate some custom tools into my project, I ran into some confusion around how to set it all up. The process of creating and registering custom tools wasn't clearly explained in the documentation, so it took a bit longer to figure that part out.

4. **Rate Limit Errors Could Be More Specific:**
   While the SDK handles rate limits well, sometimes the error messages weren’t as clear as I’d hoped. They weren’t always immediately obvious as to whether it was a rate limit issue or something else like a network problem. I had to write a custom helper function to check for specific rate limit-related keywords in the error message.

## Conclusion

Overall, I’m really happy with how the **Portialabs SDK** worked for this project. It’s a powerful tool that makes working with language models like **Mistral AI** very easy. The integration of **plan generation**, **rate limiting**, and **error handling** saved me a lot of time and effort. While there were a few bumps in the road—mainly around documentation clarity and parsing output—once I got past those hurdles, the SDK performed reliably.

---

## Installation

To use the Portialabs SDK and run the project:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/portialabs-calculator.git
