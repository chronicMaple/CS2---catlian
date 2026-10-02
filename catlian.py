import streamlit as st

# Configure the Streamlit page layout
st.set_page_config(
    page_title="Pet the Alien Cat",
    page_icon="🐱",
    layout="centered"
)

# Custom HTML, CSS, and JavaScript component
pet_cat_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pet the Alien Cat</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #f7f4ed; /* Beige-like white */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }

        .container {
            text-align: center;
            position: relative;
        }

        .instruction {
            font-size: 1.5rem;
            color: #2c3e50;
            margin-bottom: 20px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }

        /* Cat wrapper styling */
        .cat-wrapper {
            position: relative;
            display: inline-block;
            cursor: pointer;
        }

        /* Alien Cat Emoji / Graphic Container */
        .cat-face {
            font-size: 10rem;
            transition: transform 0.2s ease;
            user-select: none;
            display: inline-block;
        }

        /* Hover interaction effect */
        .cat-wrapper:hover .cat-face {
            transform: scale(1.1) rotate(5deg);
        }

        /* Floating heart elements generated via JS */
        .heart {
            position: absolute;
            font-size: 1.5rem;
            animation: floatUp 1s ease-out forwards;
            pointer-events: none;
            user-select: none;
        }

        @keyframes floatUp {
            0% {
                opacity: 1;
                transform: translateY(0) scale(0.6);
            }
            100% {
                opacity: 0;
                transform: translateY(-80px) scale(1.4);
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="instruction" id="instruction-text">pet the cat to make it happy</div>
        
        <div class="cat-wrapper" id="catWrapper">
            <!-- Sad alien cat initially -->
            <div class="cat-face" id="catFace">😿</div>
        </div>
    </div>

    <script>
        const catWrapper = document.getElementById('catWrapper');
        const catFace = document.getElementById('catFace');
        const instructionText = document.getElementById('instruction-text');

        // Mouse enter: Switch to happy face & update text
        catWrapper.addEventListener('mouseenter', () => {
            catFace.textContent = '😸';
            instructionText.textContent = 'Yay! So happy!';
            instructionText.style.color = '#27ae60';
        });

        // Mouse leave: Revert back to sad face & original text
        catWrapper.addEventListener('mouseleave', () => {
            catFace.textContent = '😿';
            instructionText.textContent = 'pet the cat to make it happy';
            instructionText.style.color = '#2c3e50';
        });

        // Mouse move over the cat: Release hearts continuously
        catWrapper.addEventListener('mousemove', (e) => {
            createHeart(e);
        });

        function createHeart(e) {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heart.innerHTML = '💖';

            // Get bounding box to position hearts relative to the wrapper container
            const rect = catWrapper.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            heart.style.left = `${x}px`;
            heart.style.top = `${y}px`;

            catWrapper.appendChild(heart);

            // Clean up the DOM node after the animation finishes (1 second)
            setTimeout(() => {
                heart.remove();
            }, 1000);
        }
    </script>
</body>
</html>
"""

# Render the component inside Streamlit with adjusted height
st.html(pet_cat_html)