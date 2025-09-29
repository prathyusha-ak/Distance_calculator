<script>
  export let label;
  export let placeholder = "Input address";
  export let value = "";
</script>

<div class="input-group">
  <label class="label">{label}</label>
  <input type="text" class="input-field" placeholder={placeholder} bind:value />
</div>

<style>
  .input-group {
    flex: 1;
    margin-right: 20px;
  }

  .input-group:last-child {
    margin-right: 0;
  }

  .label {
    display: block;
    font-size: 14px;
    color: #333;
    margin-bottom: 8px;
    font-weight: 500;
  }

  .input-field {
    width: 100%;
    padding: 10px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
    background: white;
  }

  .input-field:focus {
    outline: none;
    border-color: #007acc;
  }
</style>
