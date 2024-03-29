import { useQuery } from "@apollo/client";
import React, { ReactElement, useMemo } from "react";

import arrow from "../../assets/arrow.svg";
import { MachinesQuery, SlackProfile, UserStatsDocument } from "../../generated";
import classes from "./Stats.module.css";

type StatsProps = { machines: MachinesQuery["machines"] };

export const Stats = ({ machines }: StatsProps): ReactElement => {
  const { data: userData, loading } = useQuery(UserStatsDocument);
  const users = useMemo(
    () => (userData?.users || []).filter((user) => user.litersTotal >= 1).sort((a, b) => b.litersTotal - a.litersTotal),
    [userData]
  );

  const topMachines = useMemo(() => [...machines].sort((a, b) => b.litersTotal - a.litersTotal), [machines]);

  if (loading) return <p>Loading...</p>;

  return (
    <section className={classes.StatsByPeriod}>
      <h2>
        This year <img src={arrow} className={classes.ArrowIcon} alt="Arrow" />
      </h2>
      <table className={classes.StatsTable}>
        <thead>
          <tr>
            <th>Machine</th>
            <th>Liter</th>
            <th>Info</th>
          </tr>
        </thead>
        <tbody>
          {topMachines.map((machine) => (
            <tr key={machine.id}>
              <td>
                <img
                  className={classes.StatsTableMachineAvatar}
                  src={machine.avatarUrl}
                  alt={`${machine.name}'s avatar`}
                />
                {machine.name}
              </td>
              <td>{machine.litersTotal}&nbsp;L</td>
              <td className={classes.StatsTableInfo}>{/* TODO */}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <h3>Colleagues brewing the most</h3>
      <table className={classes.Brewers}>
        <tbody>
          {users.map((user) => (
            <tr className={classes.BrewerItem} key={user.userId}>
              <td className={classes.Brewer}>
                <img
                  className={classes.BrewerAvatar}
                  src={user.image48}
                  alt={`${user.realName || user.userId}'s avatar`}
                />
                {user.realName || user.userId}
              </td>
              <td>{user.litersTotal}&nbsp;L</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
};
