export default function Home() {
  return (
    <main style={{ padding: 32, fontFamily: "Arial" }}>
      <h1>Hospitality Operations Agent</h1>
      <p>Guest communication operations dashboard</p>

      <section>
        <h2>Incoming Guest Request</h2>
        <p>Guest: John Smith</p>
        <p>Request: My flight arrives at 1 AM. Can I still check in?</p>
      </section>

      <section>
        <h2>Agent Decision</h2>
        <p>Intent: Late check-in</p>
        <p>Decision: Approved</p>
        <p>Actions: Update arrival note, send instructions</p>
      </section>
    </main>
  );
}
