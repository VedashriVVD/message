import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Message For Gaurav ❤️",
    page_icon="💌",
    layout="centered"
)

html = """
<!DOCTYPE html>
<html>

<head>

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<style>

/* =========================
   BASIC PAGE
========================= */

* {
    box-sizing: border-box;
}

body {

    margin: 0;

    min-height: 100vh;

    overflow: hidden;

    font-family:
        "Trebuchet MS",
        Arial,
        sans-serif;

    background:
        linear-gradient(
            135deg,
            #dcecff,
            #fff4f8,
            #ffe4ee
        );

    color: #503745;

    text-align: center;
}


/* =========================
   SCREENS
========================= */

.screen {

    display: none;

    min-height: 700px;

    height: 100vh;

    align-items: center;

    justify-content: center;

    flex-direction: column;

    padding: 20px;
}


.screen.active {

    display: flex;

    animation:
        fadeIn 0.9s ease;
}


@keyframes fadeIn {

    from {

        opacity: 0;

        transform:
            scale(0.92)
            translateY(20px);

    }

    to {

        opacity: 1;

        transform:
            scale(1)
            translateY(0);

    }

}


/* =========================
   FLOATING HEARTS
========================= */

.float {

    position: fixed;

    bottom: -50px;

    font-size: 25px;

    animation:
        floatUp 7s linear infinite;

    opacity: 0.65;

    pointer-events: none;
}


.heart1 {
    left: 8%;
}

.heart2 {

    left: 28%;

    animation-delay:
        2s;
}

.heart3 {

    left: 70%;

    animation-delay:
        4s;
}

.heart4 {

    left: 90%;

    animation-delay:
        1s;
}


@keyframes floatUp {

    to {

        bottom: 110%;

        transform:
            translateX(45px)
            rotate(360deg);

    }

}


/* =========================
   SMALL TEXT
========================= */

.small-text {

    font-size: 22px;

    margin-bottom: 10px;
}


/* =========================
   ENVELOPE
========================= */

.envelope {

    width: 270px;

    height: 180px;

    background: #f49bb8;

    border-radius: 12px;

    position: relative;

    cursor: pointer;

    box-shadow:
        0 18px 35px
        rgba(100, 55, 75, 0.20);

    margin: 20px;

    transition:
        transform 0.3s ease;

}


.envelope:hover {

    transform:
        translateY(-8px)
        scale(1.04);

}


/* envelope flap */

.envelope::before {

    content: "";

    position: absolute;

    left: 0;

    top: 0;

    border-left:
        135px solid transparent;

    border-right:
        135px solid transparent;

    border-top:
        105px solid #ffc0d3;

    z-index: 3;

    transform-origin: top;

    transition:
        transform 0.8s ease;

}


/* bottom part */

.envelope::after {

    content: "";

    position: absolute;

    left: 0;

    bottom: 0;

    border-left:
        135px solid #ec779d;

    border-right:
        135px solid #ec779d;

    border-top:
        92px solid transparent;

}


/* open animation */

.envelope.open::before {

    transform:
        rotateX(180deg);

}


/* heart seal */

.seal {

    position: absolute;

    z-index: 5;

    top: 62px;

    left: 50%;

    transform:
        translateX(-50%);

    font-size: 48px;

    transition:
        0.5s ease;

}


.envelope.open .seal {

    opacity: 0;

    transform:
        translateX(-50%)
        scale(0);

}


/* =========================
   OPEN ME TEXT
========================= */

.open-text {

    font-size: 23px;

    font-weight: bold;

    animation:
        pulse 1.5s infinite;

}


@keyframes pulse {

    50% {

        transform:
            scale(1.08);

    }

}


/* =========================
   FRIEND MESSAGE SCREEN
========================= */

.friend-icon {

    font-size: 85px;

    margin-bottom: 10px;

    animation:
        gentleBounce 2s infinite;

}


@keyframes gentleBounce {

    0%, 100% {

        transform:
            translateY(0);

    }

    50% {

        transform:
            translateY(-10px);

    }

}


.friend-text {

    max-width: 650px;

    font-size: 30px;

    line-height: 1.4;

}


.highlight {

    color: #df648c;

    font-weight: bold;

}


/* =========================
   ARROW
========================= */

.arrow {

    font-size: 55px;

    cursor: pointer;

    margin: 12px;

    animation:
        arrowMove 1s infinite;

}


@keyframes arrowMove {

    50% {

        transform:
            translateY(12px);

    }

}


/* =========================
   SECOND ENVELOPE
========================= */

.second-icon {

    font-size: 65px;

    margin-bottom: 5px;

    animation:
        gentleBounce 2s infinite;

}


/* =========================
   FINAL SCREEN
========================= */

.final-heart {

    font-size: 85px;

    animation:
        heartBeat 1.2s infinite;

}


@keyframes heartBeat {

    50% {

        transform:
            scale(1.18);

    }

}


.final-title {

    font-size:
        clamp(30px, 7vw, 55px);

    margin:
        10px 0 20px;

    color: #d85c84;

}


.quote-box {

    max-width: 700px;

    background:
        rgba(
            255,
            255,
            255,
            0.78
        );

    padding:
        30px 28px;

    border-radius: 28px;

    box-shadow:
        0 15px 35px
        rgba(
            100,
            50,
            75,
            0.12
        );

    font-size: 22px;

    line-height: 1.7;

    animation:
        quoteAppear 1.5s ease;

}


@keyframes quoteAppear {

    from {

        opacity: 0;

        transform:
            translateY(45px);

    }

    to {

        opacity: 1;

        transform:
            translateY(0);

    }

}


.signature {

    margin-top: 20px;

    font-size: 20px;

    font-weight: bold;

    color: #d85c84;

}


/* =========================
   LITTLE SPARKLES
========================= */

.sparkle {

    position: fixed;

    top: -40px;

    font-size: 23px;

    animation:
        sparkleFall 5s linear infinite;

    pointer-events: none;

}


@keyframes sparkleFall {

    to {

        transform:
            translateY(110vh)
            rotate(360deg);

    }

}


/* =========================
   MOBILE
========================= */

@media(max-width:600px) {

    .envelope {

        width: 230px;

        height: 155px;

    }


    .envelope::before {

        border-left-width:
            115px;

        border-right-width:
            115px;

    }


    .envelope::after {

        border-left-width:
            115px;

        border-right-width:
            115px;

    }


    .friend-text {

        font-size: 25px;

    }


    .quote-box {

        font-size: 19px;

        padding:
            24px 20px;

    }

}

</style>

</head>


<body>


<!-- FLOATING HEARTS -->

<div class="float heart1">❤️</div>

<div class="float heart2">💕</div>

<div class="float heart3">💗</div>

<div class="float heart4">✨</div>



<!-- =================================
     SCREEN 1
================================= -->

<section
    id="screen1"
    class="screen active"
>

    <div class="small-text">

        A little message for you...

    </div>


    <div style="font-size:55px;">

        💌

    </div>


    <div
        id="envelope1"
        class="envelope"
        onclick="openFirst()"
    >

        <div class="seal">

            ❤️

        </div>

    </div>


    <div class="open-text">

        OPEN ME 💗

    </div>

</section>



<!-- =================================
     SCREEN 2
================================= -->

<section
    id="screen2"
    class="screen"
>


    <div class="friend-icon">

        🧸

    </div>


    <div class="friend-text">

        Your

        <span class="highlight">

            best friend

        </span>

        wants to tell you

        <br>

        something... ❤️

    </div>


    <div
        class="arrow"
        onclick="goToThird()"
    >

        ⬇️

    </div>


    <div style="font-size:18px;">

        Don't ignore this one... 👀

    </div>

</section>



<!-- =================================
     SCREEN 3
================================= -->

<section
    id="screen3"
    class="screen"
>


    <div class="second-icon">

        🧸💗

    </div>


    <h2>

        There's something

        <br>

        I really want you to know...

    </h2>


    <div
        id="envelope2"
        class="envelope"
        onclick="openSecond()"
    >

        <div class="seal">

            💕🧸

        </div>

    </div>


    <div class="open-text">

        OPEN THIS 💌

    </div>

</section>



<!-- =================================
     SCREEN 4
================================= -->

<section
    id="screen4"
    class="screen"
>


    <div class="final-heart">

        ❤️

    </div>


    <div class="final-title">

        Dear Gaurav...

    </div>


    <div class="quote-box">


        <b>

            No matter what,

            I'm always with you. ❤️

        </b>


        <br><br>


        Now just smile,

        cute handsome. 🥹💗


        <br><br>


        Your smile is very precious,

        so keep it always on your face. 😊❤️


        <br><br>


        You are never alone.

        <br>

        <b>

            I'm always here for you. 🤍

        </b>


        <div class="signature">

            — Your Best Friend ❤️

        </div>


    </div>


</section>



<script>


/* =========================
   CHANGE SCREEN
========================= */

function changeScreen(
    current,
    next
) {

    document
        .getElementById(current)
        .classList
        .remove("active");


    setTimeout(

        function() {

            document
                .getElementById(next)
                .classList
                .add("active");

        },

        300

    );

}



/* =========================
   FIRST ENVELOPE
========================= */

function openFirst() {

    document
        .getElementById("envelope1")
        .classList
        .add("open");


    setTimeout(

        function() {

            changeScreen(
                "screen1",
                "screen2"
            );

        },

        850

    );

}



/* =========================
   ARROW
========================= */

function goToThird() {

    changeScreen(
        "screen2",
        "screen3"
    );

}



/* =========================
   SECOND ENVELOPE
========================= */

function openSecond() {

    document
        .getElementById("envelope2")
        .classList
        .add("open");


    setTimeout(

        function() {

            changeScreen(
                "screen3",
                "screen4"
            );


            createSparkles();

        },

        850

    );

}



/* =========================
   FINAL SPARKLES
========================= */

function createSparkles() {

    const symbols = [

        "❤️",
        "💕",
        "✨",
        "💗",
        "🤍",
        "⭐",
        "🌸"

    ];


    for (

        let i = 0;

        i < 30;

        i++

    ) {

        const sparkle =
            document.createElement(
                "div"
            );


        sparkle.className =
            "sparkle";


        sparkle.innerText =
            symbols[
                Math.floor(
                    Math.random()
                    *
                    symbols.length
                )
            ];


        sparkle.style.left =
            Math.random()
            *
            100
            +
            "%";


        sparkle.style.animationDelay =
            Math.random()
            *
            4
            +
            "s";


        document
            .body
            .appendChild(
                sparkle
            );

    }

}

</script>


</body>

</html>
"""


components.html(
    html,
    height=760,
    scrolling=False
)