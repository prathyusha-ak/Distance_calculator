<script>
  import "../app.css";
  import Header from "$lib/components/Header.svelte";
  import AddressInput from "$lib/components/AddressInput.svelte";
  import UnitSelector from "$lib/components/UnitSelector.svelte";
  import CalculateButton from "$lib/components/CalculateButton.svelte";
  import HistoryButton from "$lib/components/HistoryButton.svelte";
  import HistoryTable from "$lib/components/HistoryTable.svelte";

  let sourceAddress = "";
  let destinationAddress = "";
  let selectedUnit = "miles";
  let distanceData = null;
  let loading = false;
  let error = null;
  let errorDetails = null;
  let showHistory = false;
  // Sample history data - replace with your actual data source
  //   let historyData = [
  //     {
  //       source: "New York, NY",
  //       destination: "Los Angeles, CA",
  //       distanceKms: 3944.42,
  //       distanceMiles: 2451.07,
  //     },
  //     {
  //       source: "Chicago, IL",
  //       destination: "Miami, FL",
  //       distanceKms: 1878.25,
  //       distanceMiles: 1166.89,
  //     },
  //     {
  //       source: "San Francisco, CA",
  //       destination: "Seattle, WA",
  //       distanceKms: 1094.68,
  //       distanceMiles: 679.85,
  //     },
  //     {
  //       source: "Boston, MA",
  //       destination: "Washington, DC",
  //       distanceKms: 634.45,
  //       distanceMiles: 394.14,
  //     },
  //     {
  //       source: "Denver, CO",
  //       destination: "Phoenix, AZ",
  //       distanceKms: 887.58,
  //       distanceMiles: 551.51,
  //     },
  //   ];

  let historyData = [];

  async function handleCalculate() {
    if (!sourceAddress || !destinationAddress) return;

    loading = true;
    error = null;

    try {
      // Dummy API URL - replace with your actual API endpoint
      const apiUrl = `http://127.0.0.1:8000/api/v1?source=${encodeURIComponent(sourceAddress)}&destination=${encodeURIComponent(destinationAddress)}`;

      const response = await fetch(apiUrl, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        errorDetails = await response.json();
        throw new Error(`${errorDetails.detail}`);
      }

      const data = await response.json();

      // For demo purposes, we'll simulate the expected response structure
      // Replace this with actual API response parsing
      distanceData = {
        distanceMiles: data.distanceMiles, // Random demo value
        distanceKms: data.distanceKms, // Random demo value
      };
    } catch (err) {
      error = `Calculating distance failed. Error: ${err}`;
    } finally {
      loading = false;
    }
  }

  async function toggleHistory() {
    // Toggles between true/false
    showHistory = !showHistory;
    // Fetch db data & display only when showHistory is true
    if (showHistory) {
      error = null;

      try {
        // Dummy API URL - replace with your actual API endpoint
        const apiUrl = `http://127.0.0.1:8000/api/v1/history`;

        const response = await fetch(apiUrl, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) {
          errorDetails = await response.json();
          throw new Error(`${errorDetails.detail}`);
        }
        const data = await response.json();
        historyData = data;
      } catch (err) {
        error = `Fetching history failed. Error: ${err}`;
      } finally {
        loading = false;
      }
    }
  }

  function handleCloseHistory() {
    showHistory = false;
  }
</script>

<svelte:head>
  <title>Distance Calculator</title>
</svelte:head>

<div>
  <!-- History button positioned in top-right corner -->
  <HistoryButton onClick={toggleHistory} showingHistory={showHistory} />
  <Header />
  <div class="container">
    {#if !showHistory}
      <div class="main-content">
        <div class="address-inputs">
          <AddressInput label="Source Address" bind:value={sourceAddress} />
          <AddressInput
            label="Destination Address"
            bind:value={destinationAddress}
          />
          <UnitSelector bind:selectedUnit {distanceData} {loading} />
        </div>

        <CalculateButton
          onClick={handleCalculate}
          disabled={!sourceAddress || !destinationAddress}
          {loading}
        />

        {#if error}
          <div class="error-message">{error}</div>
        {/if}
      </div>
    {/if}
    {#if showHistory}
      <HistoryTable {historyData} onClose={handleCloseHistory} />
    {/if}
  </div>
</div>

<style>
  .main-content {
    position: relative;
  }

  .address-inputs {
    display: flex;
    align-items: flex-start;
    gap: 0;
    margin-bottom: 20px;
  }

  .error-message {
    margin-top: 15px;
    padding: 10px 15px;
    background: #fee;
    border: 1px solid #fcc;
    border-radius: 4px;
    color: #c33;
    font-size: 14px;
  }

  :global(.container) {
    position: relative;
  }
</style>
