import React from "react";
import { useForm, useWatch } from "react-hook-form";
import axios from "axios";
import api from "../api";

const DisplayLiveTotal = ({ control }) => {
  const weights = useWatch({
    control,
    name: [
      "FTSE_weight",
      "SNP500_weight",
      "NIKKEI225_weight",
      "EUROSTOXX_weight",
      "HSI_weight",
    ],
    defaultValue: {
      FTSE_weight: 0,
      SNP500_weight: 0,
      NIKKEI225_weight: 0,
      EUROSTOXX_weight: 0,
      HSI_weight: 0,
    },
  });
  const total = weights.reduce((sum, v) => sum + (Number(v) || 0), 0);

  return <div>Current Total: {total.toFixed(2)}/1.00</div>;
};

const PortfoliosForm = ({ onSourceChange }) => {
  const {
    register,
    handleSubmit,
    control,
    formState: { errors },
  } = useForm({
    defaultValues: {
      investment_amount: 0,
      FTSE_weight: 0,
      SNP500_weight: 0,
      NIKKEI225_weight: 0,
      EUROSTOXX_weight: 0,
      HSI_weight: 0,
    },
  });

  const today = new Date().toISOString().split("T")[0];

  const onSubmit = async (data) => {
    try {
      const response = await api.post("/api/portfolios/", data);
      alert("Portfolio Created!");
      onSourceChange();
    } catch (error) {
      console.error("Submission failed:", error.response?.data);
    }
  };

  const onError = (errors) => console.log("Form Validation Errors:", errors);

  return (
    <form onSubmit={handleSubmit(onSubmit, onError)}>
      <div className="investment-frequency-input-field">
        <label htmlFor="investment_frequency">Investment Frequency: </label>
        <select id="investment_frequency" {...register("investment_frequency")}>
          <option value="daily">Daily</option>
          <option value="monthly">Monthly</option>
          <option value="quarterly">Quarterly</option>
          <option value="yearly">Yearly</option>
        </select>
      </div>

      <input
        type="number"
        className="amount-input"
        step="0.01"
        {...register("investment_amount", { valueAsNumber: true })}
      />

      <input
        type="date"
        className="date-input-field"
        {...register("start_date", {
          required: "A date is required",
          min: {
            value: "2015-01-01",
            message: "Date cannot be before January 1st, 2015",
          },
          max: {
            value: today,
            message: "Date cannot be in the future",
          },
        })}
      />
      {errors.start_date && <span>{errors.start_date.message}</span>}
      <input
        type="date"
        className="date-input-field"
        {...register("end_date", {
          required: "A date is required",
          min: {
            value: "2015-01-01",
            message: "Date cannot be before January 1st, 2015",
          },
          max: {
            value: today,
            message: "Date cannot be in the future",
          },
        })}
      />
      {errors.end_date && <span>{errors.end_date.message}</span>}

      <input
        type="number"
        step="0.01"
        className="weight-input"
        {...register("FTSE_weight", {
          required: "This weight is required",
          min: { value: 0, message: "Minimum is 0" },
          max: { value: 1, message: "Maximum is 1" },
          valueAsNumber: true,
        })}
      />
      {errors.FTSE_weight && <span>{errors.FTSE_weight.message}</span>}

      <input
        type="number"
        step="0.01"
        className="weight-input"
        {...register("SNP500_weight", {
          required: "This weight is required",
          min: { value: 0, message: "Minimum is 0" },
          max: { value: 1, message: "Maximum is 1" },
          valueAsNumber: true,
        })}
      />
      {errors.SNP500_weight && <span>{errors.SNP500_weight.message}</span>}

      <input
        type="number"
        step="0.01"
        className="weight-input"
        {...register("NIKKEI225_weight", {
          required: "This weight is required",
          min: { value: 0, message: "Minimum is 0" },
          max: { value: 1, message: "Maximum is 1" },
          valueAsNumber: true,
        })}
      />
      {errors.NIKKEI225_weight && (
        <span>{errors.NIKKEI225_weight.message}</span>
      )}

      <input
        type="number"
        step="0.01"
        className="weight-input"
        {...register("EUROSTOXX_weight", {
          required: "This weight is required",
          min: { value: 0, message: "Minimum is 0" },
          max: { value: 1, message: "Maximum is 1" },
          valueAsNumber: true,
        })}
      />
      {errors.EUROSTOXX_weight && (
        <span>{errors.EUROSTOXX_weight.message}</span>
      )}

      <input
        type="number"
        step="0.01"
        className="weight-input"
        {...register("HSI_weight", {
          required: "This weight is required",
          min: { value: 0, message: "Minimum is 0" },
          max: { value: 1, message: "Maximum is 1" },
          valueAsNumber: true,
        })}
      />
      {errors.HSI_weight && <span>{errors.HSI_weight.message}</span>}
      <DisplayLiveTotal control={control} />
      <button type="submit">Submit Portfolio</button>
    </form>
  );
};

export default PortfoliosForm;
