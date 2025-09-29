<script>
  export let historyData = [];
  export let loading = false;
  export let error = null;
  export let onRefresh = () => {};
</script>

<div class="history-content">
  {#if loading}
    <div class="loading-state">
      <div class="loading-spinner"></div>
      <p>Loading history...</p>
    </div>
  {:else if error}
    <div class="error-state">
      <p class="error-message">{error}</p>
      <button class="refresh-btn" on:click={onRefresh}>Try Again</button>
    </div>
  {:else if historyData.length === 0}
    <div class="no-data">
      <p>No historical queries found</p>
    </div>
  {:else}
    <div class="table-header">
      <h3>Historical Queries ({historyData.length})</h3>
    </div>
    <table class="history-table">
      <thead>
        <tr>
          <th>Source</th>
          <th>Destination</th>
          <th>Distance (KM)</th>
          <th>Distance (Miles)</th>
        </tr>
      </thead>
      <tbody>
        {#each historyData as record}
          <tr>
            <td>{record.source}</td>
            <td>{record.destination}</td>
            <td>{record.distanceKms}</td>
            <td>{record.distanceMiles}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  {/if}
</div>

<style>
  .history-content {
    width: 100%;
    padding: 30px;
    background: white;
  }

  .loading-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 60px 20px;
    color: #666;
  }

  .loading-spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #f3f3f3;
    border-top: 4px solid #007acc;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 15px;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  .error-state {
    text-align: center;
    padding: 40px 20px;
  }

  .error-message {
    color: #c33;
    margin-bottom: 15px;
    font-size: 14px;
  }

  .no-data {
    text-align: center;
    padding: 40px 20px;
    color: #666;
    font-style: italic;
  }

  .no-data p {
    margin-bottom: 15px;
  }

  .table-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .table-header h3 {
    margin: 0;
    font-size: 18px;
    color: #333;
    font-weight: 500;
  }

  .refresh-btn {
    background: #007acc;
    color: white;
    border: none;
    padding: 8px 16px;
    font-size: 13px;
    border-radius: 4px;
    cursor: pointer;
  }

  .refresh-btn:hover {
    background: #0066aa;
  }

  .refresh-btn:disabled {
    background: #ccc;
    cursor: not-allowed;
  }

  .history-table {
    width: 100%;
    border-collapse: collapse;
    background: white;
  }

  .history-table th {
    background: #f8f9fa;
    padding: 15px;
    text-align: left;
    font-weight: 600;
    color: #333;
    border-bottom: 2px solid #dee2e6;
    font-size: 14px;
  }

  .history-table td {
    padding: 15px;
    border-bottom: 1px solid #dee2e6;
    font-size: 14px;
    color: #333;
  }

  .history-table tbody tr:hover {
    background: #f8f9fa;
  }

  .history-table tbody tr:nth-child(even) {
    background: #fbfbfb;
  }

  .history-table tbody tr:nth-child(even):hover {
    background: #f0f0f0;
  }

  .history-table tbody tr:last-child td {
    border-bottom: none;
  }
</style>
