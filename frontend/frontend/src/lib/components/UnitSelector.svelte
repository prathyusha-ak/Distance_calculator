<script>
  export let selectedUnit = "miles";
  export let distanceData = null;
  export let loading = false;

  $: displayValue = getDisplayValue(selectedUnit, distanceData, loading);

  function getDisplayValue(unit, data, isLoading) {
    if (isLoading) return "Calculating...";
    if (!data) return "-";

    switch (unit) {
      case "miles":
        return `${data.distanceMiles} miles`;
      case "kilometers":
        return `${data.distanceKms} km`;
      case "both":
        return `${data.distanceMiles} miles / ${data.distanceKms} km`;
      default:
        return "-";
    }
  }
</script>

<div class="unit-selector">
  <label class="label">Unit</label>
  <div class="radio-group">
    <label class="radio-option">
      <input type="radio" bind:group={selectedUnit} value="miles" />
      Miles
    </label>
    <label class="radio-option">
      <input type="radio" bind:group={selectedUnit} value="kilometers" />
      Kilometers
    </label>
    <label class="radio-option">
      <input type="radio" bind:group={selectedUnit} value="both" />
      Both
    </label>
  </div>

  <div class="distance-display">
    <label class="label">Distance</label>
    <div class="distance-value" class:loading>{displayValue}</div>
  </div>
</div>

<style>
  .unit-selector {
    margin-left: 20px;
    min-width: 200px;
  }

  .label {
    display: block;
    font-size: 14px;
    color: #333;
    margin-bottom: 8px;
    font-weight: 500;
  }

  .radio-group {
    margin-bottom: 20px;
  }

  .radio-option {
    display: block;
    margin-bottom: 6px;
    font-size: 14px;
    color: #333;
    cursor: pointer;
  }

  .radio-option input {
    margin-right: 8px;
  }

  .distance-display {
    margin-top: 20px;
    font-weight: bold;
  }

  .distance-value {
    padding: 10px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    background: #f9f9f9;
    font-size: 14px;
    color: #666;
    text-align: center;
  }
</style>
