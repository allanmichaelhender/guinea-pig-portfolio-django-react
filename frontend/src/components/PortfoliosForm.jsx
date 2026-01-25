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

  return (
    <div className="current-total">Current Total: {total.toFixed(2)}/1.00</div>
  );
};

const PortfoliosForm = ({ isLoggedIn, onPortfolioCreated }) => {
  const {
    register,
    handleSubmit,
    control,
    formState: { errors },
  } = useForm({
    defaultValues: {
      investment_amount: 1,
      FTSE_weight: 0,
      SNP500_weight: 0,
      NIKKEI225_weight: 0,
      EUROSTOXX_weight: 0,
      HSI_weight: 0,
      end_date: new Date().toISOString().split('T')[0],
      start_date: "2015-01-01",
    },
  });

  const today = new Date().toISOString().split("T")[0];

  const onSubmit = async (data) => {
    const endpoint = isLoggedIn ? "/api/portfolios/" : "/api/portfolios-guest/";

    try {
      const response = await api.post(endpoint, data);
      onPortfolioCreated(response.data);
    } catch (error) {
      console.error("Submission failed:", error.response?.data);
    }
  };

  const onError = (errors) => console.log("Form Validation Errors:", errors);

  return (
    <form className="form-container" onSubmit={handleSubmit(onSubmit, onError)}>
      <div className="form-group">
        <label htmlFor="investment_frequency" className="form-label">
          Investment Frequency:
        </label>
        <div className="select-wrapper">
          <select
            id="investment_frequency"
            className="custom-select"
            {...register("investment_frequency")}
          >
            <option value="daily">Daily</option>
            <option value="monthly">Monthly</option>
            <option value="quarterly">Quarterly</option>
            <option value="yearly">Yearly</option>
          </select>
        </div>
      </div>

      <div className="form-group">
        <label htmlFor="investment-amount"> Investment Amount: £</label>
        <input
          id="investment-amount"
          type="number"
          className="form-input"
          step="0.01"
          {...register("investment_amount", { valueAsNumber: true })}
        />
      </div>

    <div className="form-group">
      <label htmlFor=""> Start Date:</label>
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
      </div>
      {errors.start_date && <span>{errors.start_date.message}</span>}

      <div className='form-group'>
      <label>End Date:</label>
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
      </div>
      <div className="form-group">
        <label htmlFor="FTSE_weight">FTSE Weight: </label>
        <input
          type="number"
          step="0.01"
          className="form-input"
          id="FTSE_weight"
          {...register("FTSE_weight", {
            required: "This weight is required",
            min: { value: 0, message: "Minimum is 0" },
            max: { value: 1, message: "Maximum is 1" },
            valueAsNumber: true,
          })}
        />
      </div>
      {errors.FTSE_weight && <span>{errors.FTSE_weight.message}</span>}

      <div className="form-group">
        <label htmlFor="SNP500_weight">S&P500 Weight: </label>
        <input
          type="number"
          step="0.01"
          className="form-input"
          id="SNP500_weight"
          {...register("SNP500_weight", {
            required: "This weight is required",
            min: { value: 0, message: "Minimum is 0" },
            max: { value: 1, message: "Maximum is 1" },
            valueAsNumber: true,
          })}
        />
      </div>
      {errors.SNP500_weight && <span>{errors.SNP500_weight.message}</span>}

      <div className="form-group">
        <label htmlFor="NIKKEI225_weight">NIKKEI225 Weight: </label>
        <input
          type="number"
          step="0.01"
          className="form-input"
          id="NIKKEI225_weight"
          {...register("NIKKEI225_weight", {
            required: "This weight is required",
            min: { value: 0, message: "Minimum is 0" },
            max: { value: 1, message: "Maximum is 1" },
            valueAsNumber: true,
          })}
        />
      </div>
      {errors.NIKKEI225_weight && (
        <span>{errors.NIKKEI225_weight.message}</span>
      )}

      <div className="form-group">
        <label htmlFor="EUROSTOXX_weight">EUROSTOXX Weight: </label>
        <input
          type="number"
          step="0.01"
          className="form-input"
          id="EUROSTOXX_weight"
          {...register("EUROSTOXX_weight", {
            required: "This weight is required",
            min: { value: 0, message: "Minimum is 0" },
            max: { value: 1, message: "Maximum is 1" },
            valueAsNumber: true,
          })}
        />
      </div>
      {errors.EUROSTOXX_weight && (
        <span>{errors.EUROSTOXX_weight.message}</span>
      )}

      <div className="form-group">
        <label htmlFor="HSI_weight">HSI Weight: </label>
        <input
          type="number"
          step="0.01"
          className="form-input"
          id="HSI_weight"
          {...register("HSI_weight", {
            required: "This weight is required",
            min: { value: 0, message: "Minimum is 0" },
            max: { value: 1, message: "Maximum is 1" },
            valueAsNumber: true,
          })}
        />
      </div>
      {errors.HSI_weight && <span>{errors.HSI_weight.message}</span>}

        <div className="form-group">
      <DisplayLiveTotal control={control} />
      <button className="form-button" type="submit">
        Submit
      </button>
      </div>
    </form>
  );
};

export default PortfoliosForm;
