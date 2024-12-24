async function loadSettings() {
    try {
        const response = await fetch("/settings.json");
        const settings = await response.json();
        document.getElementById("output").innerText = JSON.stringify(settings, null, 2);
    } catch (error) {
        console.error("Error loading settings:", error);
    }
}