<script>
  export let onClick = () => {};
  export let showingHistory = false;
</script>

<div class="history-container">
  <button
    class="history-btn"
    on:click={onClick}
    style="background: {showingHistory ? '#666' : 'black'}"
  >
    {showingHistory ? "Back to Calculator" : "View Historical Queries"}
    <span class="icon">{showingHistory ? "←" : "↗"}</span>
  </button>
</div>

<style>
  .history-container {
    position: absolute;
    top: 30px;
    right: 30px;
  }

  .history-btn {
    color: white;
    border: none;
    padding: 8px 16px;
    font-size: 13px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .history-btn:hover {
    background: #555;
  }

  .icon {
    font-size: 12px;
  }
</style>
