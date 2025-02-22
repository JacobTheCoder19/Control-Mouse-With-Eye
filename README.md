<h2><em>💎 Key Features 💎</em></h2>
<div>
  🟩 <strong>Eye-Controlled Mouse</strong><br>
  &emsp;🔸 Utilize your eye movements to control the mouse cursor on your laptop, providing a unique and hands-free interaction method.<br><br>
</div>
<div>
  🟩 <strong>Real-Time Tracking</strong><br>
  &emsp;🔸 The program uses a webcam to track facial landmarks in real-time, allowing for smooth and responsive cursor movement.<br><br>
</div>
<div>
  🟩 <strong>Click Functionality</strong><br>
  &emsp;🔸 Perform mouse clicks by simply blinking or closing your eyes, making it easy to interact with applications.<br><br>
</div>
<div>
  🟩 <strong>Visual Feedback</strong><br>
  &emsp;🔸 The application provides visual indicators on the screen, showing tracked eye landmarks for better user awareness.<br><br>
</div>
<div>
  🟩 <strong>Cross-Platform Compatibility</strong><br>
  &emsp;🔸 Built using Python, the program can run on various operating systems that support OpenCV and PyAutoGUI.<br><br>
</div>
<div>
  🟩 <strong>Easy Setup</strong><br>
  &emsp;🔸 Simple installation process with minimal dependencies, allowing users to get started quickly.<br><br>
</div>

<h2><em>✨ Purpose / Inspiration ✨</em></h2>
&emsp;This project was inspired by another project I made previously where I was able to control my computer with my hand. After making that last project I wanted to see if I could make it more impressive and less hands free by using my eye. It does not have as much functionality as the other program, but it still allows for hand free control of the computer which seems really futuristic and it was very fun to make!

<h2><em>⚙️ How it works ⚙️</em></h2>

&emsp;To begin, the program utilizes the OpenCV library for image processing and the MediaPipe library for detecting facial landmarks. Upon startup, it activates the webcam to capture video frames, which are then processed to identify specific points around the eyes. The program continuously tracks these points to determine the position of the mouse cursor based on eye movements.

&emsp;When the user looks at a specific landmark, the program calculates the corresponding screen coordinates and moves the mouse cursor accordingly. Additionally, the application detects when the user blinks or closes their eyes for a brief moment, triggering a mouse click. This interaction method allows for a seamless and intuitive user experience.

&emsp;The design includes visual feedback by drawing circles around the detected eye landmarks, helping users understand how their movements are being interpreted. The program runs in a loop, continuously updating the cursor position and checking for click actions until the user decides to exit. Overall, this eye-controlled mouse program showcases the capabilities of computer vision and provides an innovative solution for hands-free computer interaction.
