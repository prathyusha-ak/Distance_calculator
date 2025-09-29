<script>
  export let onClick = () => {};
  export let disabled = false;
  export let loading = false;
</script>

<button
  class="calculate-btn"
  class:disabled
  class:loading
  on:click={onClick}
  disabled={disabled || loading}
  style="background: {disabled ? '#666' : '#fa0505'}"
>
  {loading ? "Calculating..." : "Calculate Distance"}
  <span class="icon">🖩</span>
</button>

<style>
  .calculate-btn {
    /* background: #666; */
    color: white;
    border: none;
    padding: 12px 24px;
    font-size: 14px;
    cursor: pointer;
    margin-top: 20px;
    min-width: 150px;
  }

  .calculate-btn:hover:not(.disabled):not(.loading) {
    background: #555;
  }

  .calculate-btn.disabled,
  .calculate-btn.loading {
    opacity: 0.6;
    cursor: not-allowed;
  }

  .calculate-btn.loading {
    background: #007acc;
    opacity: 0.8;
  }
  .icon {
    font-size: 20px;
  }
</style>
