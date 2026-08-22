"use client";

import { useState } from "react";
import { runLateCheckinWorkflow } from "../lib/api";

export default function WorkflowTester() {
  const [message, setMessage] = useState("My flight arrives at 1 AM. Can I still check in?");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function submit() {
    setLoading(true);
    try {
      const data = await runLateCheckinWorkflow({
        guest_message: message,
        reservation_id: "R1001",
      });
      setResult(data);
    } catch (error) {
      setResult({ error: "Unable to reach workflow service" });
    }
    setLoading(false);
  }

  return (
    <div>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        rows={4}
        className="w-full border p-3"
      />

      <button
        onClick={submit}
        className="mt-3 border px-4 py-2"
      >
        {loading ? "Processing" : "Run Workflow"}
      </button>

      {result && (
        <pre className="mt-4 border p-3 text-sm">
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}
