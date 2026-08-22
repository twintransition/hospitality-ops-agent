const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function runLateCheckinWorkflow(payload: {
  guest_message: string;
  reservation_id: string;
}) {
  const response = await fetch(`${API_BASE_URL}/workflows/late-checkin`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error("Workflow request failed");
  }

  return response.json();
}
