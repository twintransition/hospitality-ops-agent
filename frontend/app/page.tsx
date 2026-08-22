import WorkflowTester from "./components/WorkflowTester";

export default function Home() {
  return (
    <main style={{ padding: 32, fontFamily: "Arial" }}>
      <h1>Hospitality Operations Agent</h1>
      <p>Guest communication operations dashboard</p>

      <WorkflowTester />
    </main>
  );
}
