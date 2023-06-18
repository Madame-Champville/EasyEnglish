const testData = [
    {
        question: "1) His eyes were ...... bad that he couldn't read the number plate of the car in front.",
        a: "such",
        b: "too",
        c: "so",
        d: "very",
        correct: "c",
    },
    {
        question: "2) The company needs to decide ...... and for all what its position is on this point.",
        a: "here",
        b: "once",
        c: "first",
        d: "finally",
        correct: "b",
    },
    {
        question: "3) Don't put your cup on the ...... of the table – someone will knock it off.",
        a: "outside",
        b: "edge",
        c: "boundary",
        d: "border",
        correct: "b",
    },
    {
        question: "4) I'm sorry - I didn't ...... to disturb you.",
        a: "hope",
        b: "think",
        c: "mean",
        d: "suppose",
        correct: "c",
    },
    {
        question: "5) The singer ended the concert ...... her most popular song.",
        a: "by",
        b: "with",
        c: "in",
        d: "as",
        correct: "b",
    },
];

const test = document.getElementById('test')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const a_text = document.getElementById('a_text')
const b_text = document.getElementById('b_text')
const c_text = document.getElementById('c_text')
const d_text = document.getElementById('d_text')
const submitBtn = document.getElementById('submit')

let currentTest = 0
let score = 0

loadTest()

function loadTest() {
    deselectAnswer()

    const currentTestData = testData[currentTest]

    questionEl.innerText = currentTestData.question
    a_text.innerText = currentTestData.a
    b_text.innerText = currentTestData.b
    c_text.innerText = currentTestData.c
    d_text.innerText = currentTestData.d
}

function deselectAnswer() {
    answerEls.forEach(answerEl => (answerEl.checked = false))
}

function getSelected() {
    let answer
    answerEls.forEach((answerEl) => {
        if (answerEl.checked) {
            answer = answerEl.id
        }
    })
    return answer
}

submitBtn.addEventListener('click', () => {
    const answer = getSelected()
    if (answer) {
        if (answer === testData[currentTest].correct) {
            score++
        }

        currentTest++

        if (currentTest < testData.length) {
            loadTest()
        } else {
            let level
            if (score === 1) {
                level = "beginner"
            } else if (score === 2) {
                level = "elementary"
            } else if (score === 3) {
                level = "pre-intermediate"
            } else if (score === 4) {
                level = "intermediate"
            } else if (score === testData.length) {
                level = "upper-intermediate"
            }

            test.innerHTML = `
            <h2>Ваш уровень ${level}</h2>
            <button onclick="location.reload()">Reload</button>
            `
        }
    }
})