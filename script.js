async function lookupOrder() {
    const orderId = document.getElementById('orderInput').value.trim();
    const email = document.getElementById('emailInput').value.trim();
    const resultDiv = document.getElementById('resultContent');
    const card = document.getElementById('resultCard');

    // Validation
    if (!orderId || !email) {
        resultDiv.innerHTML = "⚠️ Please enter both Order ID and Email.";
        card.className = 'result-card error';
        card.classList.remove('hidden');
        return;
    }

    try {
        const response = await fetch('/api/order/' + orderId);
        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = "❌ " + data.error;
            card.className = 'result-card error';
        } else {
            // Build the dashboard result card
            let html = `<strong>Order:</strong> ${data.id}<br>`;
            html += `<strong>Status:</strong> ${data.status}<br>`;
            if (data.carrier && data.tracking) {
                html += `<strong>Carrier:</strong> ${data.carrier} | <strong>Tracking:</strong> ${data.tracking}<br>`;
            }
            html += `<strong>ETA:</strong> ${data.eta}<br><hr>`;

            // Show Refund info if it exists (covers the 2nd category)
            if (data.refund) {
                html += `<strong>🔄 Refund Status:</strong> ${data.refund.refund_status}<br>`;
                html += `<strong>Refund ETA:</strong> ${data.refund.refund_eta}`;
            } else {
                html += `<em>No return requested for this order.</em>`;
            }
            resultDiv.innerHTML = html;
            card.className = 'result-card';
        }
        card.classList.remove('hidden');
    } catch (error) {
        resultDiv.innerHTML = "⚠️ Server error. Please try again later.";
        card.className = 'result-card error';
        card.classList.remove('hidden');
    }
}

// Allow "Enter" key to trigger search
document.getElementById('orderInput').addEventListener('keyup', function(event) {
    if (event.key === 'Enter') lookupOrder();
});
document.getElementById('emailInput').addEventListener('keyup', function(event) {
    if (event.key === 'Enter') lookupOrder();
});