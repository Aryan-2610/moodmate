document.addEventListener("DOMContentLoaded", () => {
    const analyzeBtn = document.getElementById("analyzeBtn");
    const userText = document.getElementById("userText");
    const resultDiv = document.getElementById("result");
    const moodSpan = document.getElementById("mood");
    const spotifyFrame = document.getElementById("spotify");
    const quoteP = document.getElementById("quote");
    const historyList = document.getElementById("historyList");

    let moodHistoryData = [];

    analyzeBtn.addEventListener("click", async () => {
        const text = userText.value.trim();
        if (!text) {
            alert("Please write something about your day!");
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:5000/analyze", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text })
            });

            const data = await response.json();
            if (data.error) {
                alert(data.error);
                return;
            }

            moodSpan.textContent = data.mood;
            quoteP.textContent = `"${data.quote}"`;
            spotifyFrame.src = data.playlist;

            moodHistoryData = data.history;

            // Update sidebar
            updateSidebar();

            resultDiv.classList.remove("hidden");
        } catch (err) {
            console.error(err);
            alert("Error analyzing mood");
        }
    });

    function updateSidebar() {
        historyList.innerHTML = "";
        if (moodHistoryData.length === 0) {
            historyList.innerHTML = "<li>No mood history yet!</li>";
        } else {
            moodHistoryData.forEach(entry => {
                const li = document.createElement("li");
                li.innerHTML = `
                    <strong>[${entry.timestamp}] ${entry.mood}</strong>
                    <details>
                        <summary>View description</summary>
                        <textarea readonly>${entry.text}</textarea>
                    </details>
                `;
                historyList.appendChild(li);
            });
        }
    }
});
